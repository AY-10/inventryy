from drf_spectacular.utils import extend_schema, OpenApiParameter
from drf_spectacular.types import OpenApiTypes

# Sale ViewSet documentation
sale_list_docs = extend_schema(
    summary="List all sales",
    description="Returns a list of all sales with pagination and filtering options.",
    parameters=[
        OpenApiParameter(
            name="store",
            type=OpenApiTypes.INT,
            description="Filter sales by store ID"
        ),
        OpenApiParameter(
            name="date_from",
            type=OpenApiTypes.DATE,
            description="Filter sales from date (YYYY-MM-DD)"
        ),
        OpenApiParameter(
            name="date_to",
            type=OpenApiTypes.DATE,
            description="Filter sales to date (YYYY-MM-DD)"
        ),
        OpenApiParameter(
            name="ordering",
            type=OpenApiTypes.STR,
            description="Order sales by field (date, total_amount)"
        )
    ],
    responses={200: "List of sales retrieved successfully"},
    tags=["Sales"]
)

sale_create_docs = extend_schema(
    summary="Create a new sale",
    description="Creates a new sale with multiple items and updates store inventory.",
    request={
        "application/json": {
            "type": "object",
            "properties": {
                "store": {"type": "integer", "description": "Store ID"},
                "date": {"type": "string", "format": "date-time", "description": "Sale date and time"},
                "customer_name": {"type": "string", "description": "Customer name"},
                "customer_email": {"type": "string", "format": "email", "description": "Customer email"},
                "items": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "product": {"type": "integer", "description": "Product ID"},
                            "quantity": {"type": "integer", "description": "Quantity sold"},
                            "unit_price": {"type": "number", "description": "Price per unit"}
                        },
                        "required": ["product", "quantity", "unit_price"]
                    }
                }
            },
            "required": ["store", "date", "items"]
        }
    },
    responses={
        201: "Sale created successfully",
        400: "Invalid input data or insufficient stock"
    },
    tags=["Sales"]
)

sale_delete_docs = extend_schema(
    summary="Delete a sale",
    description="Deletes a sale and restores the inventory quantities. This operation is only allowed for recent sales.",
    responses={
        204: "Sale deleted successfully and inventory restored",
        400: "Cannot delete old sales or sale with processed payments"
    },
    tags=["Sales"]
)

# SaleItem ViewSet documentation
sale_item_list_docs = extend_schema(
    summary="List sale items",
    description="Returns a list of all items in a sale with pagination and filtering.",
    parameters=[
        OpenApiParameter(
            name="sale",
            type=OpenApiTypes.INT,
            description="Filter items by sale ID"
        ),
        OpenApiParameter(
            name="product",
            type=OpenApiTypes.INT,
            description="Filter items by product ID"
        ),
        OpenApiParameter(
            name="ordering",
            type=OpenApiTypes.STR,
            description="Order items by field (quantity, total_price)"
        )
    ],
    responses={200: "List of sale items retrieved successfully"},
    tags=["Sale Items"]
)

sale_item_delete_docs = extend_schema(
    summary="Delete a sale item",
    description="Deletes a sale item and updates the sale total. This operation is only allowed for recent sales.",
    responses={
        204: "Sale item deleted successfully and sale total updated",
        400: "Cannot delete items from old sales or sales with processed payments"
    },
    tags=["Sale Items"]
)
