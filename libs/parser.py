from typing import Any
from libs.entities import SignUp, Class, Role, Announcement, Event

def parse_sign_up(data: dict) -> SignUp:
    return SignUp(
        id=data["id"],
        entry_time=data["entryTime"],
        name=data["name"],
        role_name=data["roleName"],
        role_emote_id=data["roleEmoteId"],
        class_name=data["className"],
        position=data["position"],
        class_emote_id=data["classEmoteId"],
        user_id=data["userId"],
        status=data["status"],
    )

def parse_class(data: dict) -> Class:
    return Class(
        name=data["name"],
        limit=data["limit"],
        emote_id=data["emoteId"],
        type=data["type"],
        specs=data.get("specs", []),
    )


def parse_role(data: dict) -> Role:
    return Role(
        name=data["name"],
        limit=data["limit"],
        emote_id=data["emoteId"],
    )


def parse_announcement(data: dict) -> Announcement:
    return Announcement(
        channel=data["channel"],
        time=data["time"],
        message=data["message"],
    )

def parse_event(data: dict) -> Event:
    return Event(
        id=data["id"],
        title=data["title"],
        display_title=data.get("displayTitle", ""),
        description=data["description"],
        template_id=data["templateId"],
        leader_id=data["leaderId"],
        leader_name=data["leaderName"],
        server_id=data["serverId"],
        channel_id=data["channelId"],
        channel_name=data["channelName"],
        channel_type=data["channelType"],
        date=data["date"],
        time=data["time"],
        color=data["color"],
        last_updated=data["lastUpdated"],
        start_time=data["startTime"],
        end_time=data["endTime"],
        closing_time=data["closingTime"],
        sign_ups=[parse_sign_up(s) for s in data.get("signUps", [])],
        classes=[parse_class(c) for c in data.get("classes", [])],
        roles=[parse_role(r) for r in data.get("roles", [])],
        announcements=[parse_announcement(a) for a in data.get("announcements", [])],
    )