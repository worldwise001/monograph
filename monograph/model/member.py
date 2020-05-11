from typing import List, Optional, Dict

import attr

from monograph.model.schema import CrossRefAttrsSchema


@attr.s(auto_attribs=True)
class MemberCounts:
    total_dois: int
    current_dois: int
    backfile_dois: int


class MemberCountsSchema(CrossRefAttrsSchema):
    class Meta:
        target = MemberCounts


@attr.s(auto_attribs=True)
class MemberDOIsByYear:
    year: int
    count: int


class MemberDOIsByYearSchema(CrossRefAttrsSchema):
    class Meta:
        target = MemberDOIsByYear


@attr.s(auto_attribs=True)
class MemberBreakdowns:
    dois_issued_by_year: List[MemberDOIsByYear]


class MemberBreakdownsSchema(CrossRefAttrsSchema):
    class Meta:
        target = MemberBreakdowns


@attr.s(auto_attribs=True)
class MemberCoverage:
    affiliations_current: float
    similarity_checking_current: float
    funders_backfile: float
    licenses_backfile: float
    funders_current: float
    affiliations_backfile: float
    resource_links_backfile: float
    orcids_backfile: float
    update_policies_current: float
    open_references_backfile: float
    orcids_current: float
    similarity_checking_backfile: float
    references_backfile: float
    award_numbers_backfile: float
    update_policies_backfile: float
    licenses_current: float
    award_numbers_current: float
    abstracts_backfile: float
    resource_links_current: float
    abstracts_current: float
    open_references_current: float
    references_current: float


class MemberCoverageSchema(CrossRefAttrsSchema):
    class Meta:
        target = MemberCoverage


@attr.s(auto_attribs=True)
class MemberPrefix:
    reference_visibility: str
    public_reference: bool
    name: str
    value: str


class MemberPrefixSchema(CrossRefAttrsSchema):
    class Meta:
        target = MemberPrefix


@attr.s(auto_attribs=True)
class MemberCountsTypeCounts:
    journal_article: str
    journal: Optional[str] = None


class MemberCountsTypeCountsSchema(CrossRefAttrsSchema):
    class Meta:
        target = MemberCountsTypeCounts


@attr.s(auto_attribs=True)
class MemberCountsType:
    all: MemberCountsTypeCounts
    current: MemberCountsTypeCounts
    backfile: MemberCountsTypeCounts


class MemberCountsTypeSchema(CrossRefAttrsSchema):
    class Meta:
        target = MemberCountsType


@attr.s(auto_attribs=True)
class Member:
    last_status_check_time: int
    primary_name: str
    counts: MemberCounts
    breakdowns: MemberBreakdowns
    prefixes: List[str]
    coverage: MemberCoverage
    prefix: List[MemberPrefix]
    id: int
    tokens: List[str]
    counts_type: MemberCountsType
    # coverage_type: MemberCoverageType
    flags: Dict[str, bool]
    location: str
    names: List[str]


class MemberSchema(CrossRefAttrsSchema):
    class Meta:
        target = Member
