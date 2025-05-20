from fastapi import APIRouter
import boto3

router = APIRouter(tags=["model"])

@router.get("/models/sagemaker-endpoints")
def list_sagemaker_endpoints():
    client = boto3.client("sagemaker")
    endpoints = []
    paginator = client.get_paginator("list_endpoints")
    for page in paginator.paginate():
        for ep in page.get("Endpoints", []):
            endpoints.append({
                "EndpointName": ep["EndpointName"],
                "EndpointStatus": ep["EndpointStatus"]
            })
    return {"endpoints": endpoints}
