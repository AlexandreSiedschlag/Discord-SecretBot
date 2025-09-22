from datetime import datetime
import requests
from libs.parser import parse_event
from collections import Counter


class RaidHelperAPI:
    def __init__(self, server_id):
        self.CHANNELS = {
            "Ping avalon": 1206977406213296228,
        }
        self.base_url = "https://raid-helper.dev/api"
        self.api_key = "2UXU5wnSzTyWp4veRccb51cqruQj1KFS0pzqHMKM"
        self.user_api_key = "m42Qrl7zYj4QwzNMpxgeqfzbnFLN8eDBIupu3933"
        self.headers = {"Authorization": f"{self.api_key}"}
        self.user_headers = {"Authorization": f"{self.user_api_key}"}
        self.server_id = server_id
    # Get
    def get_event(self, event_id, raw=True):
        url = f"{self.base_url}/v2/events/{event_id}"
        resp = requests.get(url)
        resp = parse_event(resp.json()) if raw else resp.json()
        return resp
    
    def get_events(self):
        url = f"{self.base_url}/events"
        return requests.get(url)

    def get_server_events(
        self,
        page=None,
        include_signups=None,
        channel_filter=None,
        start_time=None,
        end_time=None
    ):
        url = f"{self.base_url}/v3/servers/{self.server_id}/events"
        headers = self.headers.copy()

        if page is not None:
            headers["Page"] = str(page)
        if include_signups is not None:
            headers["IncludeSignUps"] = str(include_signups).lower()
        if channel_filter:
            headers["ChannelFilter"] = str(channel_filter)
        if start_time:
            headers["StartTimeFilter"] = str(start_time)
        if end_time:
            headers["EndTimeFilter"] = str(end_time)
        resp = requests.get(url, headers=headers)
        return resp.json()

    def get_server_scheduled_events(self):
        url = f"{self.base_url}/v3/servers/{self.server_id}/scheduledevents"
        return requests.get(url, headers=self.headers)

    def get_attendance(self):
        url = f"{self.base_url}/v2/servers/{self.server_id}/attendance"
        return requests.get(url, headers=self.headers)
    
    def get_user_events(self):
        url = f"{self.base_url}/v3/users/me/events"
        return requests.get(url, headers=self.user_headers)

    # Create
    def create_event(self, channel_id, data):
        url = f"{self.base_url}/v2/servers/{self.server_id}/channels/{channel_id}/event"
        return requests.post(url, headers=self.headers, json=data)

    def create_embed(self, channel_id, data):
        url = f"{self.base_url}/v2/servers/{self.server_id}/channels/{channel_id}/embed"
        return requests.post(url, headers=self.headers, json=data)
    
    def edit_event(self, event_id, data):
        url = f"{self.base_url}/v2/events/{event_id}"
        return requests.patch(url, headers=self.headers, json=data)

    def delete_event(self, event_id):
        url = f"{self.base_url}/v2/events/{event_id}"
        return requests.delete(url, headers=self.headers)

    def add_signup(self, event_id, data):
        url = f"{self.base_url}/v2/events/{event_id}/signups"
        return requests.post(url, headers=self.headers, json=data)

    def edit_signup(self, event_id, signup_id, data):
        url = f"{self.base_url}/v2/events/{event_id}/signups/{signup_id}"
        return requests.patch(url, headers=self.headers, json=data)

    def delete_signup(self, event_id, signup_id):
        url = f"{self.base_url}/v2/events/{event_id}/signups/{signup_id}"
        return requests.delete(url, headers=self.headers)

    def get_dkp(self, server_id, entity_id):
        url = f"{self.base_url}/v2/servers/{server_id}/entities/{entity_id}/dkp"
        return requests.get(url, headers=self.headers)

    def patch_dkp(self, server_id, entity_id, data):
        url = f"{self.base_url}/v2/servers/{server_id}/entities/{entity_id}/dkp"
        return requests.patch(url, headers=self.headers, json=data)
    