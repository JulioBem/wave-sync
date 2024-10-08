from pydantic import BaseModel
from typing import List, Optional, Dict

# events.json classes:
class Participant(BaseModel):
    id: str
    name: str
    email: str
    profilePicture: str
    status: str

class Owner(BaseModel):
    id: str
    name: str
    email: str
    profilePicture: str
    chavePix: Optional[str]

class ExpenseItem(BaseModel):
    id: int
    name: str
    cost: str
    owner: Owner
    participants: List[Participant]
    maxQuantity: int

class Location(BaseModel):
    address: str

class Author(BaseModel):
    id: str
    name: str
    email: str
    profilePicture: str
    chavePix: Optional[str] 

class Material(BaseModel):
    name: str
    
class EventsJsonFields(BaseModel):
    id: str
    title: str
    description: str
    location: Location
    date: str
    createdAt: str
    author: Author
    participants: List[Participant]
    capacity: int
    imageURI: str
    expenses: Optional[Dict]
    difficulty: str
    materials: List[Material]

class EventCreateRequest(BaseModel):
    title: str
    capacity: int
    description: Optional[str]
    location: Location  
    date: Optional[str]
    author: Owner
    difficulty: str
    materials: List[Material]

class EventAddParticipant(BaseModel):
    id: str
    name: str
    email: Optional[str]
    profilePicture: Optional[str]
    status: str

class EventAddVehicle(BaseModel):
    name: str
    cost: str
    itinerary: str
    owner: dict
    participants: List[Participant]
    maxQuantity: int

class EventAddEquipment(BaseModel):
    name: str
    cost: str
    owner: Owner
    participants: List[Participant]
    maxQuantity: int

class EventReserveEquipment(BaseModel):
    participant:Participant


class EventReserveVehicle(BaseModel):
    participant: Participant

class EventUpdateExpenseStatus(BaseModel):
    participant_id:str
    status:str

class EventUpdateEvent(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    location: Optional[Location] = None
    date: Optional[str] = None
    capacity: Optional[int] = None
    imageURI: Optional[str] = None
    difficulty: Optional[str] = None
    materials: Optional[List[Material]] = None




