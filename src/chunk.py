"""Chunking module to decompose syllabi, rules, and resources into retrieval-sized chunks.

Prepares semantic units with rich parent references and filter metadata for vector embeddings.
"""

import re
from typing import List
from src.schemas import Course, AcademicRule, Resource, Chunk


def split_text_into_chunks(text: str, max_words: int = 45) -> List[str]:
    """Split text into semantic segments bounded by sentence or semicolon boundaries."""
    # Split on sentence ends or semicolons
    raw_segments = [s.strip() for s in re.split(r"[;\n.]+", text) if s.strip()]
    chunks = []
    current_chunk = []
    current_word_count = 0

    for seg in raw_segments:
        seg_words = len(seg.split())
        if current_word_count + seg_words > max_words and current_chunk:
            chunks.append("; ".join(current_chunk) + ".")
            current_chunk = [seg]
            current_word_count = seg_words
        else:
            current_chunk.append(seg)
            current_word_count += seg_words

    if current_chunk:
        chunks.append("; ".join(current_chunk) + ".")

    return chunks if chunks else [text]


def chunk_course(course: Course) -> List[Chunk]:
    """Generate retrieval chunks from course syllabus and metadata."""
    sub_chunks = split_text_into_chunks(course.syllabus, max_words=45)
    chunks = []
    for idx, text_seg in enumerate(sub_chunks, start=1):
        chunk_text = (
            f"Course: {course.code} - {course.title} ({course.department}). "
            f"Semester {course.semester_offered}, {course.credits} Credits. "
            f"Topics: {text_seg}"
        )
        chunks.append(
            Chunk(
                chunk_id=f"CHK_{course.code}_{idx:02d}",
                parent_id=course.code,
                entity_type="course",
                title=f"{course.code} {course.title} (Part {idx})",
                text=chunk_text,
                source_url=course.source_url,
                filter_metadata={
                    "course_code": course.code,
                    "department": course.department,
                    "semester": course.semester_offered,
                    "credits": course.credits,
                    "course_type": course.course_type,
                    "prerequisites": course.prerequisites,
                    "mode": course.mode
                }
            )
        )
    return chunks


def chunk_academic_rule(rule: AcademicRule) -> List[Chunk]:
    """Generate retrieval chunk from an academic rule."""
    chunk_text = (
        f"Academic Policy [{rule.category.upper()}]: {rule.text} "
        f"(Threshold: {rule.numeric_limit if rule.numeric_limit is not None else 'N/A'}, Applies to: {rule.applies_to})"
    )
    return [
        Chunk(
            chunk_id=f"CHK_{rule.id}",
            parent_id=rule.id,
            entity_type="academic_rule",
            title=f"Rule: {rule.id}",
            text=chunk_text,
            source_url=rule.source_url,
            filter_metadata={
                "rule_id": rule.id,
                "category": rule.category,
                "numeric_limit": rule.numeric_limit,
                "applies_to": rule.applies_to
            }
        )
    ]


def chunk_resource(resource: Resource) -> List[Chunk]:
    """Generate retrieval chunk from an open learning resource."""
    chunk_text = (
        f"Learning Resource ({resource.provider}): '{resource.title}' supporting {resource.course_code}. "
        f"Skill Covered: {resource.skill_covered}. Format: {resource.format}, Duration: {resource.duration_hours} hrs. "
        f"License: {resource.licence}."
    )
    return [
        Chunk(
            chunk_id=f"CHK_{resource.id}",
            parent_id=resource.id,
            entity_type="resource",
            title=f"Resource: {resource.title}",
            text=chunk_text,
            source_url=resource.source_url,
            filter_metadata={
                "resource_id": resource.id,
                "provider": resource.provider,
                "course_code": resource.course_code,
                "skill_covered": resource.skill_covered,
                "licence": resource.licence,
                "duration_hours": resource.duration_hours,
                "url": resource.url
            }
        )
    ]


def generate_all_chunks(
    courses: List[Course],
    rules: List[AcademicRule],
    resources: List[Resource]
) -> List[Chunk]:
    """Generate combined retrieval chunks across all entities."""
    all_chunks: List[Chunk] = []
    for c in courses:
        all_chunks.extend(chunk_course(c))
    for r in rules:
        all_chunks.extend(chunk_academic_rule(r))
    for res in resources:
        all_chunks.extend(chunk_resource(res))
    return all_chunks
