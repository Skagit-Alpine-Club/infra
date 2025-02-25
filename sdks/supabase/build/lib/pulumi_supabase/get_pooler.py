# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import sys
import pulumi
import pulumi.runtime
from typing import Mapping, Optional, Union

if sys.version_info >= (3, 11):
    pass
else:
    pass
from . import _utilities

__all__ = [
    'GetPoolerResult',
    'AwaitableGetPoolerResult',
    'get_pooler',
    'get_pooler_output',
]

@pulumi.output_type
class GetPoolerResult:
    """
    A collection of values returned by getPooler.
    """
    def __init__(__self__, id=None, project_ref=None, url=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if project_ref and not isinstance(project_ref, str):
            raise TypeError("Expected argument 'project_ref' to be a str")
        pulumi.set(__self__, "project_ref", project_ref)
        if url and not isinstance(url, dict):
            raise TypeError("Expected argument 'url' to be a dict")
        pulumi.set(__self__, "url", url)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="projectRef")
    def project_ref(self) -> str:
        return pulumi.get(self, "project_ref")

    @property
    @pulumi.getter
    def url(self) -> Mapping[str, str]:
        return pulumi.get(self, "url")


class AwaitableGetPoolerResult(GetPoolerResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetPoolerResult(
            id=self.id,
            project_ref=self.project_ref,
            url=self.url)


def get_pooler(project_ref: Optional[str] = None,
               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetPoolerResult:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['projectRef'] = project_ref
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('supabase:index/getPooler:getPooler', __args__, opts=opts, typ=GetPoolerResult, package_ref=_utilities.get_package()).value

    return AwaitableGetPoolerResult(
        id=pulumi.get(__ret__, 'id'),
        project_ref=pulumi.get(__ret__, 'project_ref'),
        url=pulumi.get(__ret__, 'url'))
def get_pooler_output(project_ref: Optional[pulumi.Input[str]] = None,
                      opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetPoolerResult]:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['projectRef'] = project_ref
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('supabase:index/getPooler:getPooler', __args__, opts=opts, typ=GetPoolerResult, package_ref=_utilities.get_package())
    return __ret__.apply(lambda __response__: GetPoolerResult(
        id=pulumi.get(__response__, 'id'),
        project_ref=pulumi.get(__response__, 'project_ref'),
        url=pulumi.get(__response__, 'url')))
