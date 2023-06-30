from app.controllers.employee import router as employee_router

def include_routers(app):
    app.include_router(
        employee_router, prefix = "/api/v1/employee", tags = ['Employee']
    )