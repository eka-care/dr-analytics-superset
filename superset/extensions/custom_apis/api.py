import json
from typing import Optional

import requests
from docutils.nodes import status
from flask import request
from flask_appbuilder import expose
from superset.views.base import BaseSupersetView
from superset import app, security_manager


class CustomAPIView(BaseSupersetView):
    route_base = "/api/v1/task-status"

    @expose('/endpoint', methods=['GET'])
    @security_manager.has_access_api(['can_read'])
    def custom_endpoint(self):
        """
        A custom API endpoint that returns data
        ---
        get:
          description: >-
            Get custom data
          responses:
            200:
              description: Custom data returned successfully
              content:
                application/json:
                  schema:
                    type: object
                    properties:
                      result:
                        type: object
        """
        # Your custom logic here
        task_id: Optional[str] = request.args.get('task_id')
        resp = self.call_bnb_get_status(task_id)
        return self.json_response(resp.json(), status=resp.status_code)


    def call_bnb_get_status(self, task_id):
        url = f"http://bnb.orbi.orbi/api/check-status/?task_id={task_id}"

        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json'
        }
        response = requests.get(url, headers=headers)

        return response
