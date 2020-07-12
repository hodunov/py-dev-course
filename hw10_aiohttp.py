from aiohttp import web
import json
import requests


async def handle(request):
    response_obj = {'status': 'success'}
    return web.Response(text=json.dumps(response_obj), status=200)


async def users(request):
    try:
        response_obj = requests.get("https://reqres.in/api/users")
        return web.Response(text=json.dumps(response_obj.text), status=200)
    except Exception as e:
        response_obj = {'status': 'failed', 'message': str(e)}
        return web.Response(text=json.dumps(response_obj), status=500)


async def lists(request):
    try:
        response_obj = requests.get("https://reqres.in/api/unknown/2")
        return web.Response(text=json.dumps(response_obj.text), status=200)
    except Exception as e:
        response_obj = {'status': 'failed', 'message': str(e)}
        return web.Response(text=json.dumps(response_obj), status=500)


app = web.Application()
app.router.add_get('/', handle)
app.router.add_get('/users', users)
app.router.add_get('/list', lists)
web.run_app(app)
