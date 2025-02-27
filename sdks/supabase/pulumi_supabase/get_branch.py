# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import sys
import pulumi
import pulumi.runtime
from typing import Optional, Sequence, Union

if sys.version_info >= (3, 11):
    pass
else:
    pass
from . import _utilities
from . import outputs

__all__ = [
    'GetBranchResult',
    'AwaitableGetBranchResult',
    'get_branch',
    'get_branch_output',
]

@pulumi.output_type
class GetBranchResult:
    """
    A collection of values returned by getBranch.
    """
    def __init__(__self__, branches=None, id=None, parent_project_ref=None):
        if branches and not isinstance(branches, list):
            raise TypeError("Expected argument 'branches' to be a list")
        pulumi.set(__self__, "branches", branches)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if parent_project_ref and not isinstance(parent_project_ref, str):
            raise TypeError("Expected argument 'parent_project_ref' to be a str")
        pulumi.set(__self__, "parent_project_ref", parent_project_ref)

    @property
    @pulumi.getter
    def branches(self) -> Sequence['outputs.GetBranchBranchResult']:
        return pulumi.get(self, "branches")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="parentProjectRef")
    def parent_project_ref(self) -> str:
        return pulumi.get(self, "parent_project_ref")


class AwaitableGetBranchResult(GetBranchResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetBranchResult(
            branches=self.branches,
            id=self.id,
            parent_project_ref=self.parent_project_ref)


def get_branch(parent_project_ref: Optional[str] = None,
               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetBranchResult:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['parentProjectRef'] = parent_project_ref
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('supabase:index/getBranch:getBranch', __args__, opts=opts, typ=GetBranchResult, package_ref=_utilities.get_package()).value

    return AwaitableGetBranchResult(
        branches=pulumi.get(__ret__, 'branches'),
        id=pulumi.get(__ret__, 'id'),
        parent_project_ref=pulumi.get(__ret__, 'parent_project_ref'))
def get_branch_output(parent_project_ref: Optional[pulumi.Input[str]] = None,
                      opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetBranchResult]:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['parentProjectRef'] = parent_project_ref
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('supabase:index/getBranch:getBranch', __args__, opts=opts, typ=GetBranchResult, package_ref=_utilities.get_package())
    return __ret__.apply(lambda __response__: GetBranchResult(
        branches=pulumi.get(__response__, 'branches'),
        id=pulumi.get(__response__, 'id'),
        parent_project_ref=pulumi.get(__response__, 'parent_project_ref')))
