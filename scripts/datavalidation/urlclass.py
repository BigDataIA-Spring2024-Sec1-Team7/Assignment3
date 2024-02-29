from pydantic import ( 
    BaseModel,
    field_validator,
    ValidationError,
    ValidationInfo,
)
import re
import validators


class URLClass(BaseModel):
    topic: str
    year: int | None
    level: str
    introduction: str | None
    learning_outcomes: str | None
    summary: str | None
    link_summary: str
    link_pdf: str | None

    @field_validator('year')
    @classmethod
    def year_must_be_valid(cls, v: int) -> int:
        if v and ((v < 1800) or (v > 2024)):
            raise ValueError('year is not valid')
        return v

    @field_validator('topic', 'introduction', 'learning_outcomes', 'summary', 'level')
    @classmethod
    def text_should_not_contain_html_or_quotes(cls, v: str, info: ValidationInfo) -> str:
        if v and re.search('[\'"‘’”“]|<.*?>', v):
            raise ValueError(f'{info.field_name} contains invalid characters like quotes or html tags')
        return v
    
    @field_validator('level')
    @classmethod
    def level_must_match_pattern(cls, v: str) -> str:
        if v and re.search(r"Level\s+(I|II|III)\b", v) == None:
            raise ValueError('level is not valid')
        return v

    @field_validator('link_pdf', 'link_summary')
    @classmethod
    def link_is_valid(cls, v: str, info: ValidationInfo) -> str:
        if v and (not validators.url(v)):
            raise ValueError(f'{info.field_name} is not a valid url')
        return v