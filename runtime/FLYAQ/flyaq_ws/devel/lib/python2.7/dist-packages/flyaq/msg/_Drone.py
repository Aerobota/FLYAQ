"""autogenerated by genpy from flyaq/Drone.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import genpy
import flyaq.msg

class Drone(genpy.Message):
  _md5sum = "56e1e8c457cd00b6794878ca6f4e0be2"
  _type = "flyaq/Drone"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """string name
string type_name
Coordinate home
Move[] movements
MoveTransition[] move_transitions
string[] slot_names
int8 SAFE = 0
int8 NORMAL = 1
int8 AGGRESSIVE = 2
int8 travel_mode # enumerated above
================================================================================
MSG: flyaq/Coordinate
float32 latitude
float32 longitude
float32 altitude
float32 heading



================================================================================
MSG: flyaq/Move
string name
int8 START = 0
int8 STOP = 1
int8 TAKE_OFF = 2
int8 LAND = 3
int8 GO_TO = 4
int8 HOVER = 5
int8 CIRCLE = 6
int8 HEAD_TO = 7
int8 type # enumerate above
Action[] pre_actions
Action[] post_actions
float32 altitude # filled only in case of TakeOff move
Coordinate target_position # filled only in case of GoTo or Circle moves
int8 DIRECT = 0
int8 HORIZONTAL_FIRST = 1
int8 VERTICAL_FIRST = 2
int8 strategy # enumerated above, filled only in case of GoTo move
duration duration # filled only in case of Hover or Circle moves
float32 radius # filled only in case of Circle move
float32 circle_altitude # filled only in case of Circle move
bool clockwise # filled only in case of Circle move
float32 direction # filled only in case of HeadTo move 

================================================================================
MSG: flyaq/Action
string name
int8 DEVICE = 0
int8 FEEDBACK = 1

int8 CHECK = 2

int8 UNICAST_NOTIFY = 3

int8 MULTICAST_NOTIFY = 4

int8 BROADCAST_NOTIFY = 5

int8 type # enumerate above

string action_name # filled only in case of DeviceAction and Feedback

Parameter[] parameters # filled only in case of DeviceAction and Feedback

string slot_name # filled only in case of Notify (any kind) or CheckNotification

string[] receivers_name # filled only in case of MulticastNotify or UnicastNotify


================================================================================
MSG: flyaq/Parameter
string key
string value

================================================================================
MSG: flyaq/MoveTransition
bool is_choice # true if the move transition is a Choice move transition
string wait_for_slot_name
string from_move_name
string to_move_name
bool fluid
string condition_identifier # filled only in case of Choice move transition
string false_branch_move_name # filled only in case of Choice move transition

"""
  # Pseudo-constants
  SAFE = 0
  NORMAL = 1
  AGGRESSIVE = 2

  __slots__ = ['name','type_name','home','movements','move_transitions','slot_names','travel_mode']
  _slot_types = ['string','string','flyaq/Coordinate','flyaq/Move[]','flyaq/MoveTransition[]','string[]','int8']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       name,type_name,home,movements,move_transitions,slot_names,travel_mode

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(Drone, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.name is None:
        self.name = ''
      if self.type_name is None:
        self.type_name = ''
      if self.home is None:
        self.home = flyaq.msg.Coordinate()
      if self.movements is None:
        self.movements = []
      if self.move_transitions is None:
        self.move_transitions = []
      if self.slot_names is None:
        self.slot_names = []
      if self.travel_mode is None:
        self.travel_mode = 0
    else:
      self.name = ''
      self.type_name = ''
      self.home = flyaq.msg.Coordinate()
      self.movements = []
      self.move_transitions = []
      self.slot_names = []
      self.travel_mode = 0

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self.name
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.type_name
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_4f.pack(_x.home.latitude, _x.home.longitude, _x.home.altitude, _x.home.heading))
      length = len(self.movements)
      buff.write(_struct_I.pack(length))
      for val1 in self.movements:
        _x = val1.name
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.pack('<I%ss'%length, length, _x))
        buff.write(_struct_b.pack(val1.type))
        length = len(val1.pre_actions)
        buff.write(_struct_I.pack(length))
        for val2 in val1.pre_actions:
          _x = val2.name
          length = len(_x)
          if python3 or type(_x) == unicode:
            _x = _x.encode('utf-8')
            length = len(_x)
          buff.write(struct.pack('<I%ss'%length, length, _x))
          buff.write(_struct_b.pack(val2.type))
          _x = val2.action_name
          length = len(_x)
          if python3 or type(_x) == unicode:
            _x = _x.encode('utf-8')
            length = len(_x)
          buff.write(struct.pack('<I%ss'%length, length, _x))
          length = len(val2.parameters)
          buff.write(_struct_I.pack(length))
          for val3 in val2.parameters:
            _x = val3.key
            length = len(_x)
            if python3 or type(_x) == unicode:
              _x = _x.encode('utf-8')
              length = len(_x)
            buff.write(struct.pack('<I%ss'%length, length, _x))
            _x = val3.value
            length = len(_x)
            if python3 or type(_x) == unicode:
              _x = _x.encode('utf-8')
              length = len(_x)
            buff.write(struct.pack('<I%ss'%length, length, _x))
          _x = val2.slot_name
          length = len(_x)
          if python3 or type(_x) == unicode:
            _x = _x.encode('utf-8')
            length = len(_x)
          buff.write(struct.pack('<I%ss'%length, length, _x))
          length = len(val2.receivers_name)
          buff.write(_struct_I.pack(length))
          for val3 in val2.receivers_name:
            length = len(val3)
            if python3 or type(val3) == unicode:
              val3 = val3.encode('utf-8')
              length = len(val3)
            buff.write(struct.pack('<I%ss'%length, length, val3))
        length = len(val1.post_actions)
        buff.write(_struct_I.pack(length))
        for val2 in val1.post_actions:
          _x = val2.name
          length = len(_x)
          if python3 or type(_x) == unicode:
            _x = _x.encode('utf-8')
            length = len(_x)
          buff.write(struct.pack('<I%ss'%length, length, _x))
          buff.write(_struct_b.pack(val2.type))
          _x = val2.action_name
          length = len(_x)
          if python3 or type(_x) == unicode:
            _x = _x.encode('utf-8')
            length = len(_x)
          buff.write(struct.pack('<I%ss'%length, length, _x))
          length = len(val2.parameters)
          buff.write(_struct_I.pack(length))
          for val3 in val2.parameters:
            _x = val3.key
            length = len(_x)
            if python3 or type(_x) == unicode:
              _x = _x.encode('utf-8')
              length = len(_x)
            buff.write(struct.pack('<I%ss'%length, length, _x))
            _x = val3.value
            length = len(_x)
            if python3 or type(_x) == unicode:
              _x = _x.encode('utf-8')
              length = len(_x)
            buff.write(struct.pack('<I%ss'%length, length, _x))
          _x = val2.slot_name
          length = len(_x)
          if python3 or type(_x) == unicode:
            _x = _x.encode('utf-8')
            length = len(_x)
          buff.write(struct.pack('<I%ss'%length, length, _x))
          length = len(val2.receivers_name)
          buff.write(_struct_I.pack(length))
          for val3 in val2.receivers_name:
            length = len(val3)
            if python3 or type(val3) == unicode:
              val3 = val3.encode('utf-8')
              length = len(val3)
            buff.write(struct.pack('<I%ss'%length, length, val3))
        buff.write(_struct_f.pack(val1.altitude))
        _v1 = val1.target_position
        _x = _v1
        buff.write(_struct_4f.pack(_x.latitude, _x.longitude, _x.altitude, _x.heading))
        buff.write(_struct_b.pack(val1.strategy))
        _v2 = val1.duration
        _x = _v2
        buff.write(_struct_2i.pack(_x.secs, _x.nsecs))
        _x = val1
        buff.write(_struct_2fBf.pack(_x.radius, _x.circle_altitude, _x.clockwise, _x.direction))
      length = len(self.move_transitions)
      buff.write(_struct_I.pack(length))
      for val1 in self.move_transitions:
        buff.write(_struct_B.pack(val1.is_choice))
        _x = val1.wait_for_slot_name
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.pack('<I%ss'%length, length, _x))
        _x = val1.from_move_name
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.pack('<I%ss'%length, length, _x))
        _x = val1.to_move_name
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.pack('<I%ss'%length, length, _x))
        buff.write(_struct_B.pack(val1.fluid))
        _x = val1.condition_identifier
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.pack('<I%ss'%length, length, _x))
        _x = val1.false_branch_move_name
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.pack('<I%ss'%length, length, _x))
      length = len(self.slot_names)
      buff.write(_struct_I.pack(length))
      for val1 in self.slot_names:
        length = len(val1)
        if python3 or type(val1) == unicode:
          val1 = val1.encode('utf-8')
          length = len(val1)
        buff.write(struct.pack('<I%ss'%length, length, val1))
      buff.write(_struct_b.pack(self.travel_mode))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.home is None:
        self.home = flyaq.msg.Coordinate()
      if self.movements is None:
        self.movements = None
      if self.move_transitions is None:
        self.move_transitions = None
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.name = str[start:end].decode('utf-8')
      else:
        self.name = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.type_name = str[start:end].decode('utf-8')
      else:
        self.type_name = str[start:end]
      _x = self
      start = end
      end += 16
      (_x.home.latitude, _x.home.longitude, _x.home.altitude, _x.home.heading,) = _struct_4f.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.movements = []
      for i in range(0, length):
        val1 = flyaq.msg.Move()
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.name = str[start:end].decode('utf-8')
        else:
          val1.name = str[start:end]
        start = end
        end += 1
        (val1.type,) = _struct_b.unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.pre_actions = []
        for i in range(0, length):
          val2 = flyaq.msg.Action()
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            val2.name = str[start:end].decode('utf-8')
          else:
            val2.name = str[start:end]
          start = end
          end += 1
          (val2.type,) = _struct_b.unpack(str[start:end])
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            val2.action_name = str[start:end].decode('utf-8')
          else:
            val2.action_name = str[start:end]
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          val2.parameters = []
          for i in range(0, length):
            val3 = flyaq.msg.Parameter()
            start = end
            end += 4
            (length,) = _struct_I.unpack(str[start:end])
            start = end
            end += length
            if python3:
              val3.key = str[start:end].decode('utf-8')
            else:
              val3.key = str[start:end]
            start = end
            end += 4
            (length,) = _struct_I.unpack(str[start:end])
            start = end
            end += length
            if python3:
              val3.value = str[start:end].decode('utf-8')
            else:
              val3.value = str[start:end]
            val2.parameters.append(val3)
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            val2.slot_name = str[start:end].decode('utf-8')
          else:
            val2.slot_name = str[start:end]
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          val2.receivers_name = []
          for i in range(0, length):
            start = end
            end += 4
            (length,) = _struct_I.unpack(str[start:end])
            start = end
            end += length
            if python3:
              val3 = str[start:end].decode('utf-8')
            else:
              val3 = str[start:end]
            val2.receivers_name.append(val3)
          val1.pre_actions.append(val2)
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.post_actions = []
        for i in range(0, length):
          val2 = flyaq.msg.Action()
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            val2.name = str[start:end].decode('utf-8')
          else:
            val2.name = str[start:end]
          start = end
          end += 1
          (val2.type,) = _struct_b.unpack(str[start:end])
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            val2.action_name = str[start:end].decode('utf-8')
          else:
            val2.action_name = str[start:end]
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          val2.parameters = []
          for i in range(0, length):
            val3 = flyaq.msg.Parameter()
            start = end
            end += 4
            (length,) = _struct_I.unpack(str[start:end])
            start = end
            end += length
            if python3:
              val3.key = str[start:end].decode('utf-8')
            else:
              val3.key = str[start:end]
            start = end
            end += 4
            (length,) = _struct_I.unpack(str[start:end])
            start = end
            end += length
            if python3:
              val3.value = str[start:end].decode('utf-8')
            else:
              val3.value = str[start:end]
            val2.parameters.append(val3)
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            val2.slot_name = str[start:end].decode('utf-8')
          else:
            val2.slot_name = str[start:end]
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          val2.receivers_name = []
          for i in range(0, length):
            start = end
            end += 4
            (length,) = _struct_I.unpack(str[start:end])
            start = end
            end += length
            if python3:
              val3 = str[start:end].decode('utf-8')
            else:
              val3 = str[start:end]
            val2.receivers_name.append(val3)
          val1.post_actions.append(val2)
        start = end
        end += 4
        (val1.altitude,) = _struct_f.unpack(str[start:end])
        _v3 = val1.target_position
        _x = _v3
        start = end
        end += 16
        (_x.latitude, _x.longitude, _x.altitude, _x.heading,) = _struct_4f.unpack(str[start:end])
        start = end
        end += 1
        (val1.strategy,) = _struct_b.unpack(str[start:end])
        _v4 = val1.duration
        _x = _v4
        start = end
        end += 8
        (_x.secs, _x.nsecs,) = _struct_2i.unpack(str[start:end])
        _x = val1
        start = end
        end += 13
        (_x.radius, _x.circle_altitude, _x.clockwise, _x.direction,) = _struct_2fBf.unpack(str[start:end])
        val1.clockwise = bool(val1.clockwise)
        self.movements.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.move_transitions = []
      for i in range(0, length):
        val1 = flyaq.msg.MoveTransition()
        start = end
        end += 1
        (val1.is_choice,) = _struct_B.unpack(str[start:end])
        val1.is_choice = bool(val1.is_choice)
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.wait_for_slot_name = str[start:end].decode('utf-8')
        else:
          val1.wait_for_slot_name = str[start:end]
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.from_move_name = str[start:end].decode('utf-8')
        else:
          val1.from_move_name = str[start:end]
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.to_move_name = str[start:end].decode('utf-8')
        else:
          val1.to_move_name = str[start:end]
        start = end
        end += 1
        (val1.fluid,) = _struct_B.unpack(str[start:end])
        val1.fluid = bool(val1.fluid)
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.condition_identifier = str[start:end].decode('utf-8')
        else:
          val1.condition_identifier = str[start:end]
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.false_branch_move_name = str[start:end].decode('utf-8')
        else:
          val1.false_branch_move_name = str[start:end]
        self.move_transitions.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.slot_names = []
      for i in range(0, length):
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1 = str[start:end].decode('utf-8')
        else:
          val1 = str[start:end]
        self.slot_names.append(val1)
      start = end
      end += 1
      (self.travel_mode,) = _struct_b.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self.name
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.type_name
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_4f.pack(_x.home.latitude, _x.home.longitude, _x.home.altitude, _x.home.heading))
      length = len(self.movements)
      buff.write(_struct_I.pack(length))
      for val1 in self.movements:
        _x = val1.name
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.pack('<I%ss'%length, length, _x))
        buff.write(_struct_b.pack(val1.type))
        length = len(val1.pre_actions)
        buff.write(_struct_I.pack(length))
        for val2 in val1.pre_actions:
          _x = val2.name
          length = len(_x)
          if python3 or type(_x) == unicode:
            _x = _x.encode('utf-8')
            length = len(_x)
          buff.write(struct.pack('<I%ss'%length, length, _x))
          buff.write(_struct_b.pack(val2.type))
          _x = val2.action_name
          length = len(_x)
          if python3 or type(_x) == unicode:
            _x = _x.encode('utf-8')
            length = len(_x)
          buff.write(struct.pack('<I%ss'%length, length, _x))
          length = len(val2.parameters)
          buff.write(_struct_I.pack(length))
          for val3 in val2.parameters:
            _x = val3.key
            length = len(_x)
            if python3 or type(_x) == unicode:
              _x = _x.encode('utf-8')
              length = len(_x)
            buff.write(struct.pack('<I%ss'%length, length, _x))
            _x = val3.value
            length = len(_x)
            if python3 or type(_x) == unicode:
              _x = _x.encode('utf-8')
              length = len(_x)
            buff.write(struct.pack('<I%ss'%length, length, _x))
          _x = val2.slot_name
          length = len(_x)
          if python3 or type(_x) == unicode:
            _x = _x.encode('utf-8')
            length = len(_x)
          buff.write(struct.pack('<I%ss'%length, length, _x))
          length = len(val2.receivers_name)
          buff.write(_struct_I.pack(length))
          for val3 in val2.receivers_name:
            length = len(val3)
            if python3 or type(val3) == unicode:
              val3 = val3.encode('utf-8')
              length = len(val3)
            buff.write(struct.pack('<I%ss'%length, length, val3))
        length = len(val1.post_actions)
        buff.write(_struct_I.pack(length))
        for val2 in val1.post_actions:
          _x = val2.name
          length = len(_x)
          if python3 or type(_x) == unicode:
            _x = _x.encode('utf-8')
            length = len(_x)
          buff.write(struct.pack('<I%ss'%length, length, _x))
          buff.write(_struct_b.pack(val2.type))
          _x = val2.action_name
          length = len(_x)
          if python3 or type(_x) == unicode:
            _x = _x.encode('utf-8')
            length = len(_x)
          buff.write(struct.pack('<I%ss'%length, length, _x))
          length = len(val2.parameters)
          buff.write(_struct_I.pack(length))
          for val3 in val2.parameters:
            _x = val3.key
            length = len(_x)
            if python3 or type(_x) == unicode:
              _x = _x.encode('utf-8')
              length = len(_x)
            buff.write(struct.pack('<I%ss'%length, length, _x))
            _x = val3.value
            length = len(_x)
            if python3 or type(_x) == unicode:
              _x = _x.encode('utf-8')
              length = len(_x)
            buff.write(struct.pack('<I%ss'%length, length, _x))
          _x = val2.slot_name
          length = len(_x)
          if python3 or type(_x) == unicode:
            _x = _x.encode('utf-8')
            length = len(_x)
          buff.write(struct.pack('<I%ss'%length, length, _x))
          length = len(val2.receivers_name)
          buff.write(_struct_I.pack(length))
          for val3 in val2.receivers_name:
            length = len(val3)
            if python3 or type(val3) == unicode:
              val3 = val3.encode('utf-8')
              length = len(val3)
            buff.write(struct.pack('<I%ss'%length, length, val3))
        buff.write(_struct_f.pack(val1.altitude))
        _v5 = val1.target_position
        _x = _v5
        buff.write(_struct_4f.pack(_x.latitude, _x.longitude, _x.altitude, _x.heading))
        buff.write(_struct_b.pack(val1.strategy))
        _v6 = val1.duration
        _x = _v6
        buff.write(_struct_2i.pack(_x.secs, _x.nsecs))
        _x = val1
        buff.write(_struct_2fBf.pack(_x.radius, _x.circle_altitude, _x.clockwise, _x.direction))
      length = len(self.move_transitions)
      buff.write(_struct_I.pack(length))
      for val1 in self.move_transitions:
        buff.write(_struct_B.pack(val1.is_choice))
        _x = val1.wait_for_slot_name
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.pack('<I%ss'%length, length, _x))
        _x = val1.from_move_name
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.pack('<I%ss'%length, length, _x))
        _x = val1.to_move_name
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.pack('<I%ss'%length, length, _x))
        buff.write(_struct_B.pack(val1.fluid))
        _x = val1.condition_identifier
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.pack('<I%ss'%length, length, _x))
        _x = val1.false_branch_move_name
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.pack('<I%ss'%length, length, _x))
      length = len(self.slot_names)
      buff.write(_struct_I.pack(length))
      for val1 in self.slot_names:
        length = len(val1)
        if python3 or type(val1) == unicode:
          val1 = val1.encode('utf-8')
          length = len(val1)
        buff.write(struct.pack('<I%ss'%length, length, val1))
      buff.write(_struct_b.pack(self.travel_mode))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.home is None:
        self.home = flyaq.msg.Coordinate()
      if self.movements is None:
        self.movements = None
      if self.move_transitions is None:
        self.move_transitions = None
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.name = str[start:end].decode('utf-8')
      else:
        self.name = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.type_name = str[start:end].decode('utf-8')
      else:
        self.type_name = str[start:end]
      _x = self
      start = end
      end += 16
      (_x.home.latitude, _x.home.longitude, _x.home.altitude, _x.home.heading,) = _struct_4f.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.movements = []
      for i in range(0, length):
        val1 = flyaq.msg.Move()
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.name = str[start:end].decode('utf-8')
        else:
          val1.name = str[start:end]
        start = end
        end += 1
        (val1.type,) = _struct_b.unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.pre_actions = []
        for i in range(0, length):
          val2 = flyaq.msg.Action()
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            val2.name = str[start:end].decode('utf-8')
          else:
            val2.name = str[start:end]
          start = end
          end += 1
          (val2.type,) = _struct_b.unpack(str[start:end])
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            val2.action_name = str[start:end].decode('utf-8')
          else:
            val2.action_name = str[start:end]
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          val2.parameters = []
          for i in range(0, length):
            val3 = flyaq.msg.Parameter()
            start = end
            end += 4
            (length,) = _struct_I.unpack(str[start:end])
            start = end
            end += length
            if python3:
              val3.key = str[start:end].decode('utf-8')
            else:
              val3.key = str[start:end]
            start = end
            end += 4
            (length,) = _struct_I.unpack(str[start:end])
            start = end
            end += length
            if python3:
              val3.value = str[start:end].decode('utf-8')
            else:
              val3.value = str[start:end]
            val2.parameters.append(val3)
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            val2.slot_name = str[start:end].decode('utf-8')
          else:
            val2.slot_name = str[start:end]
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          val2.receivers_name = []
          for i in range(0, length):
            start = end
            end += 4
            (length,) = _struct_I.unpack(str[start:end])
            start = end
            end += length
            if python3:
              val3 = str[start:end].decode('utf-8')
            else:
              val3 = str[start:end]
            val2.receivers_name.append(val3)
          val1.pre_actions.append(val2)
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.post_actions = []
        for i in range(0, length):
          val2 = flyaq.msg.Action()
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            val2.name = str[start:end].decode('utf-8')
          else:
            val2.name = str[start:end]
          start = end
          end += 1
          (val2.type,) = _struct_b.unpack(str[start:end])
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            val2.action_name = str[start:end].decode('utf-8')
          else:
            val2.action_name = str[start:end]
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          val2.parameters = []
          for i in range(0, length):
            val3 = flyaq.msg.Parameter()
            start = end
            end += 4
            (length,) = _struct_I.unpack(str[start:end])
            start = end
            end += length
            if python3:
              val3.key = str[start:end].decode('utf-8')
            else:
              val3.key = str[start:end]
            start = end
            end += 4
            (length,) = _struct_I.unpack(str[start:end])
            start = end
            end += length
            if python3:
              val3.value = str[start:end].decode('utf-8')
            else:
              val3.value = str[start:end]
            val2.parameters.append(val3)
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            val2.slot_name = str[start:end].decode('utf-8')
          else:
            val2.slot_name = str[start:end]
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          val2.receivers_name = []
          for i in range(0, length):
            start = end
            end += 4
            (length,) = _struct_I.unpack(str[start:end])
            start = end
            end += length
            if python3:
              val3 = str[start:end].decode('utf-8')
            else:
              val3 = str[start:end]
            val2.receivers_name.append(val3)
          val1.post_actions.append(val2)
        start = end
        end += 4
        (val1.altitude,) = _struct_f.unpack(str[start:end])
        _v7 = val1.target_position
        _x = _v7
        start = end
        end += 16
        (_x.latitude, _x.longitude, _x.altitude, _x.heading,) = _struct_4f.unpack(str[start:end])
        start = end
        end += 1
        (val1.strategy,) = _struct_b.unpack(str[start:end])
        _v8 = val1.duration
        _x = _v8
        start = end
        end += 8
        (_x.secs, _x.nsecs,) = _struct_2i.unpack(str[start:end])
        _x = val1
        start = end
        end += 13
        (_x.radius, _x.circle_altitude, _x.clockwise, _x.direction,) = _struct_2fBf.unpack(str[start:end])
        val1.clockwise = bool(val1.clockwise)
        self.movements.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.move_transitions = []
      for i in range(0, length):
        val1 = flyaq.msg.MoveTransition()
        start = end
        end += 1
        (val1.is_choice,) = _struct_B.unpack(str[start:end])
        val1.is_choice = bool(val1.is_choice)
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.wait_for_slot_name = str[start:end].decode('utf-8')
        else:
          val1.wait_for_slot_name = str[start:end]
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.from_move_name = str[start:end].decode('utf-8')
        else:
          val1.from_move_name = str[start:end]
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.to_move_name = str[start:end].decode('utf-8')
        else:
          val1.to_move_name = str[start:end]
        start = end
        end += 1
        (val1.fluid,) = _struct_B.unpack(str[start:end])
        val1.fluid = bool(val1.fluid)
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.condition_identifier = str[start:end].decode('utf-8')
        else:
          val1.condition_identifier = str[start:end]
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.false_branch_move_name = str[start:end].decode('utf-8')
        else:
          val1.false_branch_move_name = str[start:end]
        self.move_transitions.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.slot_names = []
      for i in range(0, length):
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1 = str[start:end].decode('utf-8')
        else:
          val1 = str[start:end]
        self.slot_names.append(val1)
      start = end
      end += 1
      (self.travel_mode,) = _struct_b.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_B = struct.Struct("<B")
_struct_f = struct.Struct("<f")
_struct_b = struct.Struct("<b")
_struct_2fBf = struct.Struct("<2fBf")
_struct_4f = struct.Struct("<4f")
_struct_2i = struct.Struct("<2i")
