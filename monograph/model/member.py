import datetime
import logging
from typing import List, Optional, Dict, Any

import attr
from marshmallow import pre_load, post_dump

from monograph.model.schema import CrossRefAttrsSchema

LOGGER = logging.getLogger(__name__)


@attr.s(auto_attribs=True)
class MemberCounts:
    total_dois: int
    current_dois: int
    backfile_dois: int


class MemberCountsSchema(CrossRefAttrsSchema):
    class Meta:
        target = MemberCounts
        register_as_scheme = True


@attr.s(auto_attribs=True)
class MemberDOIsByYear:
    year: Optional[int] = None
    count: Optional[int] = None


class MemberDOIsByYearSchema(CrossRefAttrsSchema):
    class Meta:
        target = MemberDOIsByYear
        register_as_scheme = True


@attr.s(auto_attribs=True)
class MemberBreakdowns:
    dois_by_issued_year: List[MemberDOIsByYear]


class MemberBreakdownsSchema(CrossRefAttrsSchema):
    class Meta:
        target = MemberBreakdowns
        register_as_scheme = True

    @pre_load
    def preload(self, data: Dict[str, Any], **kwargs: Any) -> Dict[str, Any]:
        if 'dois_by_issued_year' in data:
            doi_list = data['dois_by_issued_year']
            data['dois_by_issued_year'] = [{'year': part[0], 'count': part[1]} for part in doi_list]
        return super().preload(data)

    @post_dump
    def postdump(self, data: Dict[str, Any], **kwargs: Any) -> Dict[str, Any]:
        if 'dois_by_issued_year' in data:
            doi_list = data['dois_by_issued_year']
            data['dois_by_issued_year'] = [[part.year, part.count] for part in doi_list]
        return super().postdump(data)


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
        register_as_scheme = True


@attr.s(auto_attribs=True)
class MemberPrefix:
    reference_visibility: str
    public_reference: Optional[bool]
    name: str
    value: str


class MemberPrefixSchema(CrossRefAttrsSchema):
    class Meta:
        target = MemberPrefix
        register_as_scheme = True


@attr.s(auto_attribs=True)
class MemberCoverageSubType:
    last_status_check_time: int
    affiliations: float
    abstracts: float
    orcids: float
    licenses: float
    references: float
    funders: float
    similarity_checking: float
    award_numbers: float
    update_policies: float
    resource_links: float
    open_references: float


class MemberCoverageSubTypeSchema(CrossRefAttrsSchema):
    class Meta:
        target = MemberCoverageSubType
        register_as_scheme = True


@attr.s(auto_attribs=True)
class MemberCoverageOrCountType:
    # TODO: fix to properly allow subtypes
    journal_article: Optional[str] = None
    journal: Optional[str] = None


class MemberCoverageOrCountTypeSchema(CrossRefAttrsSchema):
    class Meta:
        target = MemberCoverageOrCountType
        register_as_scheme = True


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
    counts_type: MemberCoverageOrCountType
    coverage_type: MemberCoverageOrCountType
    flags: Dict[str, bool]
    location: str
    names: List[str]

    def get_simple(self) -> Dict[str, Any]:
        current_year = datetime.datetime.now().year
        dois = {year: 0 for year in range(current_year, current_year - 5, -1)}
        for entry in self.breakdowns.dois_by_issued_year:
            if entry.year in dois:
                dois[entry.year] = entry.count or 0
        return {
            'id': self.id,
            'name': self.primary_name,
            'dois_by_year': dois,
            'doi_prefixes': self.prefixes,
            'available_works': self.counts.current_dois,
            'last_updated': self.last_status_check_time,
            'last_updated_human_readable':
                str(datetime.datetime.now() - datetime.datetime.fromtimestamp(self.last_status_check_time / 1000))
        }


class MemberSchema(CrossRefAttrsSchema):
    class Meta:
        target = Member
        register_as_scheme = True
