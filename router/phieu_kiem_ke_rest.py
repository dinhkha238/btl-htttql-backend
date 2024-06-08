from fastapi import APIRouter

from model.feedback import FeedbackBase

router = APIRouter()

# @router.get("/feedback-by-id-product/{product_id}", tags=["Feedback"])
# async def get_feedback_by_id_product(product_id: int):
#     feedback = feedback_by_id_product(product_id) 
#     return feedback
