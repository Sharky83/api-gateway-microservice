from fastapi import FastAPI, Request, HTTPException
import httpx

app = FastAPI()

from config import BACKEND_SERVICES

@app.api_route("/proxy/{service}/{path:path}", methods=["GET", "POST", "PUT", "DELETE"])
async def proxy(service: str, path: str, request: Request):
    if service not in BACKEND_SERVICES:
        raise HTTPException(status_code=404, detail="Service not found")
    backend_url = f"{BACKEND_SERVICES[service]}/{path}"
    async with httpx.AsyncClient() as client:
        # Forward method, headers, and body
        req_method = request.method.lower()
        req_headers = dict(request.headers)
        req_body = await request.body()
        try:
            resp = await client.request(
                req_method,
                backend_url,
                headers=req_headers,
                content=req_body,
                timeout=10.0
            )
        except httpx.RequestError as e:
            raise HTTPException(status_code=502, detail=f"Upstream error: {str(e)}")
        return resp.text, resp.status_code, resp.headers.items()
