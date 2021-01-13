# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from mgrpc import ipam_pb2 as mgrpc_dot_ipam__pb2


class DeviceServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetDeviceMsg = channel.unary_unary(
                '/rpc.DeviceService/GetDeviceMsg',
                request_serializer=mgrpc_dot_ipam__pb2.ByIpRequest.SerializeToString,
                response_deserializer=mgrpc_dot_ipam__pb2.GetDeviceMsgResponse.FromString,
                )
        self.ListDeviceMsg = channel.stream_unary(
                '/rpc.DeviceService/ListDeviceMsg',
                request_serializer=mgrpc_dot_ipam__pb2.ByIpRequest.SerializeToString,
                response_deserializer=mgrpc_dot_ipam__pb2.ListDeviceMsgResponse.FromString,
                )
        self.GetDeviceSubnet = channel.unary_unary(
                '/rpc.DeviceService/GetDeviceSubnet',
                request_serializer=mgrpc_dot_ipam__pb2.ByEmptyRequest.SerializeToString,
                response_deserializer=mgrpc_dot_ipam__pb2.GetDeviceSubnetResponse.FromString,
                )


class DeviceServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetDeviceMsg(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListDeviceMsg(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetDeviceSubnet(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DeviceServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetDeviceMsg': grpc.unary_unary_rpc_method_handler(
                    servicer.GetDeviceMsg,
                    request_deserializer=mgrpc_dot_ipam__pb2.ByIpRequest.FromString,
                    response_serializer=mgrpc_dot_ipam__pb2.GetDeviceMsgResponse.SerializeToString,
            ),
            'ListDeviceMsg': grpc.stream_unary_rpc_method_handler(
                    servicer.ListDeviceMsg,
                    request_deserializer=mgrpc_dot_ipam__pb2.ByIpRequest.FromString,
                    response_serializer=mgrpc_dot_ipam__pb2.ListDeviceMsgResponse.SerializeToString,
            ),
            'GetDeviceSubnet': grpc.unary_unary_rpc_method_handler(
                    servicer.GetDeviceSubnet,
                    request_deserializer=mgrpc_dot_ipam__pb2.ByEmptyRequest.FromString,
                    response_serializer=mgrpc_dot_ipam__pb2.GetDeviceSubnetResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'rpc.DeviceService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class DeviceService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetDeviceMsg(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/rpc.DeviceService/GetDeviceMsg',
            mgrpc_dot_ipam__pb2.ByIpRequest.SerializeToString,
            mgrpc_dot_ipam__pb2.GetDeviceMsgResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListDeviceMsg(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/rpc.DeviceService/ListDeviceMsg',
            mgrpc_dot_ipam__pb2.ByIpRequest.SerializeToString,
            mgrpc_dot_ipam__pb2.ListDeviceMsgResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetDeviceSubnet(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/rpc.DeviceService/GetDeviceSubnet',
            mgrpc_dot_ipam__pb2.ByEmptyRequest.SerializeToString,
            mgrpc_dot_ipam__pb2.GetDeviceSubnetResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)