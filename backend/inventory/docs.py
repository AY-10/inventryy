from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
from drf_spectacular.types import OpenApiTypes

# Category ViewSet documentation
category_list_docs = extend_schema(
    summary="List all categories",
    description="Returns a list of all product categories with pagination.",
    responses={200: "List of categories retrieved successfully"},
    tags=["Categories"]
)

category_create_docs = extend_schema(
    summary="Create a new category",
    description="Creates a new product category.",
    request={
        "application/json": {
            "type": "object",
            "properties": {
                "name": {"type": "string", "description": "Category name"},
                "description": {"type": "string", "description": "Category description"}
            },
            "required": ["name"]
        }
    },
    responses={
        201: "Category created successfully",
        400: "Invalid input data"
    },
    tags=["Categories"]
)

category_delete_docs = extend_schema(
    summary="Delete a category",
    description="Deletes a category. This will fail if there are products associated with this category.",
    responses={
        204: "Category deleted successfully",
        400: "Cannot delete category with associated products"
    },
    tags=["Categories"]
)

# Product ViewSet documentation
product_list_docs = extend_schema(
    summary="List all products",
    description="Returns a list of all products with pagination and filtering options.",
    parameters=[
        OpenApiParameter(
            name="category",
            type=OpenApiTypes.INT,
            description="Filter products by category ID"
        ),
        OpenApiParameter(
            name="search",
            type=OpenApiTypes.STR,
            description="Search products by name, description, SKU, or barcode"
        ),
        OpenApiParameter(
            name="ordering",
            type=OpenApiTypes.STR,
            description="Order products by field (name, price, created_at)"
        )
    ],
    responses={200: "List of products retrieved successfully"},
    tags=["Products"]
)

product_create_docs = extend_schema(
    summary="Create a new product",
    description="Creates a new product with optional barcode and image.",
    request={
        "multipart/form-data": {
            "type": "object",
            "properties": {
                "name": {"type": "string", "description": "Product name"},
                "description": {"type": "string", "description": "Product description"},
                "category": {"type": "integer", "description": "Category ID"},
                "sku": {"type": "string", "description": "Stock Keeping Unit"},
                "barcode": {"type": "string", "description": "Product barcode"},
                "image": {"type": "string", "format": "binary", "description": "Product image"},
                "price": {"type": "number", "description": "Product price"}
            },
            "required": ["name", "category", "sku", "price"]
        }
    },
    responses={
        201: "Product created successfully",
        400: "Invalid input data"
    },
    tags=["Products"]
)

product_delete_docs = extend_schema(
    summary="Delete a product",
    description="Deletes a product. This will fail if there are sales or stock entries associated with this product.",
    responses={
        204: "Product deleted successfully",
        400: "Cannot delete product with associated sales or stock"
    },
    tags=["Products"]
)

# Stock ViewSet documentation
stock_list_docs = extend_schema(
    summary="List all stock entries",
    description="Returns a list of all stock entries with pagination and filtering options.",
    parameters=[
        OpenApiParameter(
            name="product",
            type=OpenApiTypes.INT,
            description="Filter stock by product ID"
        ),
        OpenApiParameter(
            name="search",
            type=OpenApiTypes.STR,
            description="Search stock by product name"
        ),
        OpenApiParameter(
            name="ordering",
            type=OpenApiTypes.STR,
            description="Order stock by field (quantity, last_updated)"
        )
    ],
    responses={200: "List of stock entries retrieved successfully"},
    tags=["Stock"]
)

stock_update_docs = extend_schema(
    summary="Update stock quantity",
    description="Updates the quantity of a product in stock.",
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
        200: "Stock updated successfully",
        400: "Invalid input data"
    },
    tags=["Stock"]
)

stock_delete_docs = extend_schema(
    summary="Delete a stock entry",
    description="Deletes a stock entry. This will fail if there are sales associated with this stock entry.",
    responses={
        204: "Stock entry deleted successfully",
        400: "Cannot delete stock entry with associated sales"
    },
    tags=["Stock"]
)
