# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from src.main.middlewares.grpc_middlewares.protos.user.list_user_inventory_proto import list_user_inventory_pb2 as list__user__inventory__pb2


class ListUserInventoryStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.makeListUserInventoryFactory = channel.unary_unary(
                '/list_user_inventory.ListUserInventory/makeListUserInventoryFactory',
                request_serializer=list__user__inventory__pb2.Request.SerializeToString,
                response_deserializer=list__user__inventory__pb2.Response.FromString,
                )


class ListUserInventoryServicer(object):
    """Missing associated documentation comment in .proto file."""

    def makeListUserInventoryFactory(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ListUserInventoryServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'makeListUserInventoryFactory': grpc.unary_unary_rpc_method_handler(
                    servicer.makeListUserInventoryFactory,
                    request_deserializer=list__user__inventory__pb2.Request.FromString,
                    response_serializer=list__user__inventory__pb2.Response.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'list_user_inventory.ListUserInventory', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ListUserInventory(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def makeListUserInventoryFactory(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/list_user_inventory.ListUserInventory/makeListUserInventoryFactory',
            list__user__inventory__pb2.Request.SerializeToString,
            list__user__inventory__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
