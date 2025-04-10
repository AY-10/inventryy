from drf_spectacular.utils import extend_schema, OpenApiParameter
from drf_spectacular.types import OpenApiTypes

# Store ViewSet documentation
store_list_docs = extend_schema(
    summary="List all stores",
    description="Returns a list of all stores with pagination and filtering options.",
    parameters=[
        OpenApiParameter(
            name="search",
            type=OpenApiTypes.STR,
            description="Search stores by name or location"
        ),
        OpenApiParameter(
            name="ordering",
            type=OpenApiTypes.STR,
            description="Order stores by field (name, created_at)"
        )
    ],
    responses={200: "List of stores retrieved successfully"},
    tags=["Stores"]
)

store_create_docs = extend_schema(
    summary="Create a new store",
    description="Creates a new store with location and contact information.",
    request={
        "application/json": {
            "type": "object",
            "properties": {
                "name": {"type": "string", "description": "Store name"},
                "location": {"type": "string", "description": "Store location"},
                "contact_number": {"type": "string", "description": "Contact phone number"},
                "email": {"type": "string", "format": "email", "description": "Contact email"},
                "address": {"type": "string", "description": "Store address"}
            },
            "required": ["name", "location"]
        }
    },
    responses={
        201: "Store created successfully",
        400: "Invalid input data"
    },
    tags=["Stores"]
)

store_delete_docs = extend_schema(
    summary="Delete a store",
    description="Deletes a store. This will fail if there are sales or inventory entries associated with this store.",
    responses={
        204: "Store deleted successfully",
        400: "Cannot delete store with associated sales or inventory"
    },
    tags=["Stores"]
)

# StoreInventory ViewSet documentation
store_inventory_list_docs = extend_schema(
    summary="List store inventory",
    description="Returns a list of all products in a store's inventory with pagination and filtering.",
    parameters=[
        OpenApiParameter(
            name="store",
            type=OpenApiTypes.INT,
            description="Filter inventory by store ID"
        ),
        OpenApiParameter(
            name="product",
            type=OpenApiTypes.INT,
            description="Filter inventory by product ID"
        ),
        OpenApiParameter(
            name="search",
            type=OpenApiTypes.STR,
            description="Search inventory by product name"
        ),
        OpenApiParameter(
            name="ordering",
            type=OpenApiTypes.STR,
            description="Order inventory by field (quantity, last_updated)"
        )
    ],
    responses={200: "List of store inventory retrieved successfully"},
    tags=["Store Inventory"]
)

store_inventory_update_docs = extend_schema(
    summary="Update store inventory",
    description="Updates the quantity of a product in a store's inventory.",
    request={
        "application/json": {
            "type": "object",
            "properties": {
                "quantity": {"type": "integer", "description": "New stock quantity"},
                "reorder_level": {"type": "integer", "description": "Reorder level threshold"},
                "reorder_quantity": {"type": "integer", "description": "Quantity to reorder"}
            },
            "required": ["quantity"]
        }
    },
    responses={
        200: "Store inventory updated successfully",
        400: "Invalid input data"
    },
    tags=["Store Inventory"]
)

store_inventory_delete_docs = extend_schema(
    summary="Delete a store inventory entry",
    description="Deletes a store inventory entry. This will fail if there are sales associated with this inventory entry.",
    responses={
        204: "Store inventory entry deleted successfully",
        400: "Cannot delete inventory entry with associated sales"
    },
    tags=["Store Inventory"]
)
