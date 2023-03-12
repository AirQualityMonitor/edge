from pydantic import BaseModel, validator


class Metric(BaseModel):
    name: str
    unit: str
    value: float

    @validator("name")
    def name_must_contain_space(cls, v):
        if " " in v:
            raise ValueError("must not contain a space")
        elif len(v) < 1 or len(v) > 7:
            raise ValueError("name should contain from 1 to 7 characters")
        return v
