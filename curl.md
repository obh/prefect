<details open>
<summary>Create a run for a deployment</summary>
<details>
<summary>Request</summary>

```
curl --request POST \
  --url http://127.0.0.1:4200/api/deployments/40686597-8f53-49e5-94b7-5b04446a39c2/create_flow_run \
  --header 'Content-Type: application/json' \
  --data '{
  "state": {
    "type": "SCHEDULED",
    "name": "deployment-run",
    "message": "Run started",
    "data": null,
    "state_details": {
      "flow_run_id": "ad45a578-ec24-4062-9323-4b1919b75b1a",
      "task_run_id": "7f0ef9d7-e7b5-4d52-8247-ce8351652f8b",
      "child_flow_run_id": "da812b02-15bb-48a9-8a93-bfcf654f163d",
      "run_input_keyset": {
        "property1": "string",
        "property2": "string"
      },
      "refresh_cache": true,
      "retriable": true
    },
    "timestamp": "2023-08-24T14:15:22Z",
    "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08"
  },
  "name": "my-flow-run",
  "parameters": {},
  "context": {
    "my_var": "my_val"
  },
  "empirical_policy": {
    "max_retries": 0,
    "retry_delay_seconds": 0,
    "retries": 0,
    "retry_delay": 0,
    "pause_keys": [
      null
    ],
    "resuming": false
  },
  "tags": [
    "tag-1",
    "tag-2"
  ]
}'
```
</details>
<details>
<summary>Response</summary>
```{
	"id": "d5861f3d-27c7-41b0-958a-d162c9a9eb78",
	"created": "2024-01-22T03:51:26.507659+00:00",
	"updated": "2024-01-22T03:51:26.518000+00:00",
	"name": "my-flow-run",
	"flow_id": "c77255ed-cf8b-480f-bca4-588fe0ab9e75",
	"state_id": "46fb1142-9f47-41dd-8e17-5f918cedffc9",
	"deployment_id": "40686597-8f53-49e5-94b7-5b04446a39c2",
	"work_queue_id": null,
	"work_queue_name": null,
	"flow_version": null,
	"parameters": {},
	"idempotency_key": null,
	"context": {
		"my_var": "my_val"
	},
	"empirical_policy": {
		"max_retries": 0,
		"retry_delay_seconds": 0.0,
		"retries": 0,
		"retry_delay": 0,
		"pause_keys": [
			null
		],
		"resuming": false
	},
	"tags": [
		"tag-2",
		"tag-1"
	],
	"parent_task_run_id": null,
	"state_type": "SCHEDULED",
	"state_name": "deployment-run",
	"run_count": 0,
	"expected_start_time": "2024-01-22T03:51:26.507402+00:00",
	"next_scheduled_start_time": "2024-01-22T03:51:26.507402+00:00",
	"start_time": null,
	"end_time": null,
	"total_run_time": 0.0,
	"estimated_run_time": 0.0,
	"estimated_start_time_delta": 0.014453,
	"auto_scheduled": false,
	"infrastructure_document_id": null,
	"infrastructure_pid": null,
	"created_by": null,
	"work_pool_id": null,
	"work_pool_name": null,
	"state": {
		"id": "46fb1142-9f47-41dd-8e17-5f918cedffc9",
		"type": "SCHEDULED",
		"name": "deployment-run",
		"timestamp": "2024-01-22T03:51:26.507282+00:00",
		"message": "Run started",
		"data": null,
		"state_details": {
			"flow_run_id": "d5861f3d-27c7-41b0-958a-d162c9a9eb78",
			"task_run_id": "7f0ef9d7-e7b5-4d52-8247-ce8351652f8b",
			"child_flow_run_id": "da812b02-15bb-48a9-8a93-bfcf654f163d",
			"scheduled_time": "2024-01-22T03:51:26.507402+00:00",
			"cache_key": null,
			"cache_expiration": null,
			"untrackable_result": false,
			"pause_timeout": null,
			"pause_reschedule": false,
			"pause_key": null,
			"run_input_keyset": {
				"property1": "string",
				"property2": "string"
			},
			"refresh_cache": true,
			"retriable": true
		}
	}
}```
</details>
</details>
