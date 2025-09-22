from dataclasses import dataclass
from typing import List, Dict, Optional

@dataclass
class SignUp:
    id: int
    entry_time: int
    name: str
    role_name: str
    role_emote_id: str
    class_name: str
    position: int
    class_emote_id: str
    user_id: str
    status: str

@dataclass
class Class:
    name: str
    limit: int
    emote_id: str
    type: str
    specs: List

@dataclass
class Role:
    name: str
    limit: int
    emote_id: str

@dataclass
class Announcement:
    channel: str
    time: str
    message: str

    
@dataclass
class Event:
    id: str
    title: str
    display_title: str
    description: str
    template_id: str
    leader_id: str
    leader_name: str
    server_id: str
    channel_id: str
    channel_name: str
    channel_type: str
    date: str
    time: str
    color: str
    last_updated: int
    start_time: int
    end_time: int
    closing_time: int
    sign_ups: List[SignUp]
    classes: List[Class]
    roles: List[Role]
    announcements: List[Announcement]