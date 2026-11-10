"""Pydantic schemas for the Adobe Personalized Learning Buddy knowledge base.

Strict schema models enforcing types, source-tracing, and validation constraints.
"""

from typing import List, Optional, Literal
from pydantic import BaseModel, Field, HttpUrl


class BaseEntity(BaseModel):
    """Base model with mandatory source provenance tracking."""
    source_url: str = Field(..., description="Official public or openly licensed URL")
    retrieved_on: str = Field(..., description="Date retrieved in YYYY-MM-DD format")
    source_type: Literal["official", "open-licence", "manual"] = Field(
        ..., description="Provenance classification of the entity"
    )


class Course(BaseEntity):
    """Course entity modeling the academic curriculum."""
    code: str = Field(..., description="Normalized course code (e.g. CSL100)")
    title: str = Field(..., description="Official course name")
    department: str = Field(..., description="Academic department or discipline")
    credits: float = Field(..., gt=0, description="Numeric credits assigned to the course")
    semester_offered: int = Field(..., ge=1, le=8, description="Standard curriculum semester (1-8)")
    course_type: Literal["core", "elective", "open"] = Field(..., description="Nature of the course")
    mode: Literal["offline", "online", "hybrid"] = Field("offline", description="Delivery mode")
    prerequisites: List[str] = Field(default_factory=list, description="List of course codes required")
    syllabus: str = Field(..., min_length=10, description="Syllabus and learning objectives")


class PrerequisiteEdge(BaseModel):
    """Explicit directional prerequisite relationship."""
    course: str = Field(..., description="Target course code")
    requires: str = Field(..., description="Prerequisite course code that must be cleared")
    kind: Literal["hard", "recommended"] = Field("hard", description="Strictness of prerequisite")


class Skill(BaseModel):
    """Skill entity for goal matching and gap diagnosis."""
    id: str = Field(..., description="Unique skill identifier (e.g. SKILL_DSA)")
    name: str = Field(..., description="Human readable skill name")
    category: str = Field(..., description="Skill category, e.g. Algorithms, Systems, AI")
    parent_skill: Optional[str] = Field(None, description="Parent skill ID if hierarchical")


class CourseSkillLink(BaseModel):
    """Mapping between course and skill acquired."""
    course: str = Field(..., description="Course code")
    skill_id: str = Field(..., description="Skill identifier")
    depth: Literal["intro", "working", "advanced"] = Field("working", description="Proficiency depth")


class AcademicRule(BaseEntity):
    """Academic rule entity representing official institute policy."""
    id: str = Field(..., description="Unique identifier for the academic rule")
    category: Literal[
        "graduation",
        "curriculum_distribution",
        "credit_limit",
        "prerequisites",
        "registration",
        "online_credits",
        "credit_validity"
    ] = Field(..., description="Policy category")
    text: str = Field(..., description="Verbatim or quotable text of the rule")
    numeric_limit: Optional[float] = Field(None, description="Numeric threshold or boundary if applicable")
    applies_to: str = Field(..., description="Target program or population")


class Resource(BaseEntity):
    """Open educational learning resource (NPTEL, MIT OCW)."""
    id: str = Field(..., description="Unique resource ID (e.g. RES_NPTEL_CSL100_01)")
    title: str = Field(..., description="Resource title")
    provider: Literal["NPTEL", "MIT OpenCourseWare", "SWAYAM"] = Field(..., description="Platform provider")
    course_code: str = Field(..., description="Course code this resource maps to")
    skill_covered: str = Field(..., description="Primary skill or competency covered")
    licence: str = Field(..., description="Open license name (e.g. CC-BY-SA 4.0)")
    format: str = Field(..., description="Media format: video_lectures, course_materials, etc.")
    duration_hours: float = Field(..., gt=0, description="Approximate duration in hours")
    url: str = Field(..., description="Publicly accessible URL")


class Chunk(BaseModel):
    """Retrieval-sized chunk ready for downstream embedding and semantic search."""
    chunk_id: str = Field(..., description="Deterministic chunk ID (e.g. CHK_CSL100_01)")
    parent_id: str = Field(..., description="ID of source entity (Course code, Rule ID, Resource ID)")
    entity_type: Literal["course", "academic_rule", "resource"] = Field(
        ..., description="Type of source entity"
    )
    title: str = Field(..., description="Reference title")
    text: str = Field(..., min_length=15, description="Chunk content for embedding")
    source_url: str = Field(..., description="Provenance URL")
    filter_metadata: dict = Field(
        default_factory=dict,
        description="Structured key-value metadata for vector/hybrid filtering"
    )
