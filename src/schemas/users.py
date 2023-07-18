# JSON-schema for /api/users

users_get_json_schema = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "meta": {
      "type": "object",
      "properties": {
        "limit": {
          "type": "integer"
        },
        "offset": {
          "type": "integer"
        },
        "total": {
          "type": "integer"
        }
      },
      "required": [
        "limit",
        "offset",
        "total"
      ]
    },
    "data": {
      "type": "array",
      "items": [
        {
          "type": "object",
          "properties": {
            "first_name": {
              "type": "string"
            },
            "last_name": {
              "type": "string"
            },
            "company_id": {
              "type": "integer"
            },
            "user_id": {
              "type": "integer"
            }
          },
          "required": [
            "first_name",
            "last_name",
            "company_id",
            "user_id"
          ]
        }
      ]
    }
  },
  "required": [
    "meta",
    "data"
  ]
}


user_post_json_schema = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "first_name": {
      "type": "string"
    },
    "last_name": {
      "type": "string"
    },
    "company_id": {
      "type": "integer"
    }
  },
  "required": [
    "first_name",
    "last_name",
    "company_id"
  ]
}