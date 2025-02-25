# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import sys
import pulumi
import pulumi.runtime
from typing import Optional, overload
if sys.version_info >= (3, 11):
    pass
else:
    pass
from . import _utilities

__all__ = ['ProjectArgs', 'Project']

@pulumi.input_type
class ProjectArgs:
    def __init__(__self__, *,
                 database_password: pulumi.Input[str],
                 organization_id: pulumi.Input[str],
                 region: pulumi.Input[str],
                 instance_size: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Project resource.
        :param pulumi.Input[str] database_password: Password for the project database
        :param pulumi.Input[str] organization_id: Reference to the organization
        :param pulumi.Input[str] region: Region where the project is located
        :param pulumi.Input[str] instance_size: Desired instance size of the project
        :param pulumi.Input[str] name: Name of the project
        """
        pulumi.set(__self__, "database_password", database_password)
        pulumi.set(__self__, "organization_id", organization_id)
        pulumi.set(__self__, "region", region)
        if instance_size is not None:
            pulumi.set(__self__, "instance_size", instance_size)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="databasePassword")
    def database_password(self) -> pulumi.Input[str]:
        """
        Password for the project database
        """
        return pulumi.get(self, "database_password")

    @database_password.setter
    def database_password(self, value: pulumi.Input[str]):
        pulumi.set(self, "database_password", value)

    @property
    @pulumi.getter(name="organizationId")
    def organization_id(self) -> pulumi.Input[str]:
        """
        Reference to the organization
        """
        return pulumi.get(self, "organization_id")

    @organization_id.setter
    def organization_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "organization_id", value)

    @property
    @pulumi.getter
    def region(self) -> pulumi.Input[str]:
        """
        Region where the project is located
        """
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: pulumi.Input[str]):
        pulumi.set(self, "region", value)

    @property
    @pulumi.getter(name="instanceSize")
    def instance_size(self) -> Optional[pulumi.Input[str]]:
        """
        Desired instance size of the project
        """
        return pulumi.get(self, "instance_size")

    @instance_size.setter
    def instance_size(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "instance_size", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the project
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _ProjectState:
    def __init__(__self__, *,
                 database_password: Optional[pulumi.Input[str]] = None,
                 instance_size: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 organization_id: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Project resources.
        :param pulumi.Input[str] database_password: Password for the project database
        :param pulumi.Input[str] instance_size: Desired instance size of the project
        :param pulumi.Input[str] name: Name of the project
        :param pulumi.Input[str] organization_id: Reference to the organization
        :param pulumi.Input[str] region: Region where the project is located
        """
        if database_password is not None:
            pulumi.set(__self__, "database_password", database_password)
        if instance_size is not None:
            pulumi.set(__self__, "instance_size", instance_size)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if organization_id is not None:
            pulumi.set(__self__, "organization_id", organization_id)
        if region is not None:
            pulumi.set(__self__, "region", region)

    @property
    @pulumi.getter(name="databasePassword")
    def database_password(self) -> Optional[pulumi.Input[str]]:
        """
        Password for the project database
        """
        return pulumi.get(self, "database_password")

    @database_password.setter
    def database_password(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "database_password", value)

    @property
    @pulumi.getter(name="instanceSize")
    def instance_size(self) -> Optional[pulumi.Input[str]]:
        """
        Desired instance size of the project
        """
        return pulumi.get(self, "instance_size")

    @instance_size.setter
    def instance_size(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "instance_size", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the project
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="organizationId")
    def organization_id(self) -> Optional[pulumi.Input[str]]:
        """
        Reference to the organization
        """
        return pulumi.get(self, "organization_id")

    @organization_id.setter
    def organization_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "organization_id", value)

    @property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[str]]:
        """
        Region where the project is located
        """
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "region", value)


class Project(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 database_password: Optional[pulumi.Input[str]] = None,
                 instance_size: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 organization_id: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a Project resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] database_password: Password for the project database
        :param pulumi.Input[str] instance_size: Desired instance size of the project
        :param pulumi.Input[str] name: Name of the project
        :param pulumi.Input[str] organization_id: Reference to the organization
        :param pulumi.Input[str] region: Region where the project is located
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ProjectArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a Project resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param ProjectArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ProjectArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 database_password: Optional[pulumi.Input[str]] = None,
                 instance_size: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 organization_id: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ProjectArgs.__new__(ProjectArgs)

            if database_password is None and not opts.urn:
                raise TypeError("Missing required property 'database_password'")
            __props__.__dict__["database_password"] = None if database_password is None else pulumi.Output.secret(database_password)
            __props__.__dict__["instance_size"] = instance_size
            __props__.__dict__["name"] = name
            if organization_id is None and not opts.urn:
                raise TypeError("Missing required property 'organization_id'")
            __props__.__dict__["organization_id"] = organization_id
            if region is None and not opts.urn:
                raise TypeError("Missing required property 'region'")
            __props__.__dict__["region"] = region
        secret_opts = pulumi.ResourceOptions(additional_secret_outputs=["databasePassword"])
        opts = pulumi.ResourceOptions.merge(opts, secret_opts)
        super(Project, __self__).__init__(
            'supabase:index/project:Project',
            resource_name,
            __props__,
            opts,
            package_ref=_utilities.get_package())

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            database_password: Optional[pulumi.Input[str]] = None,
            instance_size: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            organization_id: Optional[pulumi.Input[str]] = None,
            region: Optional[pulumi.Input[str]] = None) -> 'Project':
        """
        Get an existing Project resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] database_password: Password for the project database
        :param pulumi.Input[str] instance_size: Desired instance size of the project
        :param pulumi.Input[str] name: Name of the project
        :param pulumi.Input[str] organization_id: Reference to the organization
        :param pulumi.Input[str] region: Region where the project is located
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ProjectState.__new__(_ProjectState)

        __props__.__dict__["database_password"] = database_password
        __props__.__dict__["instance_size"] = instance_size
        __props__.__dict__["name"] = name
        __props__.__dict__["organization_id"] = organization_id
        __props__.__dict__["region"] = region
        return Project(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="databasePassword")
    def database_password(self) -> pulumi.Output[str]:
        """
        Password for the project database
        """
        return pulumi.get(self, "database_password")

    @property
    @pulumi.getter(name="instanceSize")
    def instance_size(self) -> pulumi.Output[Optional[str]]:
        """
        Desired instance size of the project
        """
        return pulumi.get(self, "instance_size")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the project
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="organizationId")
    def organization_id(self) -> pulumi.Output[str]:
        """
        Reference to the organization
        """
        return pulumi.get(self, "organization_id")

    @property
    @pulumi.getter
    def region(self) -> pulumi.Output[str]:
        """
        Region where the project is located
        """
        return pulumi.get(self, "region")

