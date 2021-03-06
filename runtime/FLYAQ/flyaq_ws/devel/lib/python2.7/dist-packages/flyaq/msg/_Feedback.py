"""autogenerated by genpy from flyaq/Feedback.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class Feedback(genpy.Message):
  _md5sum = "0e4c4d5eb3b453fc011856d2f2bcfc94"
  _type = "flyaq/Feedback"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """float32 latitude
float32 longitude
float32 altitude
float32 speed
string status
string msg 
float32 battery_percentage
float32 battery_voltage
float32 pitch
float32 roll
float32 yaw
float32 heading
string drone # the drone providing the feedback

"""
  __slots__ = ['latitude','longitude','altitude','speed','status','msg','battery_percentage','battery_voltage','pitch','roll','yaw','heading','drone']
  _slot_types = ['float32','float32','float32','float32','string','string','float32','float32','float32','float32','float32','float32','string']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       latitude,longitude,altitude,speed,status,msg,battery_percentage,battery_voltage,pitch,roll,yaw,heading,drone

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(Feedback, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.latitude is None:
        self.latitude = 0.
      if self.longitude is None:
        self.longitude = 0.
      if self.altitude is None:
        self.altitude = 0.
      if self.speed is None:
        self.speed = 0.
      if self.status is None:
        self.status = ''
      if self.msg is None:
        self.msg = ''
      if self.battery_percentage is None:
        self.battery_percentage = 0.
      if self.battery_voltage is None:
        self.battery_voltage = 0.
      if self.pitch is None:
        self.pitch = 0.
      if self.roll is None:
        self.roll = 0.
      if self.yaw is None:
        self.yaw = 0.
      if self.heading is None:
        self.heading = 0.
      if self.drone is None:
        self.drone = ''
    else:
      self.latitude = 0.
      self.longitude = 0.
      self.altitude = 0.
      self.speed = 0.
      self.status = ''
      self.msg = ''
      self.battery_percentage = 0.
      self.battery_voltage = 0.
      self.pitch = 0.
      self.roll = 0.
      self.yaw = 0.
      self.heading = 0.
      self.drone = ''

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
      _x = self
      buff.write(_struct_4f.pack(_x.latitude, _x.longitude, _x.altitude, _x.speed))
      _x = self.status
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.msg
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_6f.pack(_x.battery_percentage, _x.battery_voltage, _x.pitch, _x.roll, _x.yaw, _x.heading))
      _x = self.drone
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      _x = self
      start = end
      end += 16
      (_x.latitude, _x.longitude, _x.altitude, _x.speed,) = _struct_4f.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.status = str[start:end].decode('utf-8')
      else:
        self.status = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.msg = str[start:end].decode('utf-8')
      else:
        self.msg = str[start:end]
      _x = self
      start = end
      end += 24
      (_x.battery_percentage, _x.battery_voltage, _x.pitch, _x.roll, _x.yaw, _x.heading,) = _struct_6f.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.drone = str[start:end].decode('utf-8')
      else:
        self.drone = str[start:end]
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
      _x = self
      buff.write(_struct_4f.pack(_x.latitude, _x.longitude, _x.altitude, _x.speed))
      _x = self.status
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.msg
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_6f.pack(_x.battery_percentage, _x.battery_voltage, _x.pitch, _x.roll, _x.yaw, _x.heading))
      _x = self.drone
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      _x = self
      start = end
      end += 16
      (_x.latitude, _x.longitude, _x.altitude, _x.speed,) = _struct_4f.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.status = str[start:end].decode('utf-8')
      else:
        self.status = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.msg = str[start:end].decode('utf-8')
      else:
        self.msg = str[start:end]
      _x = self
      start = end
      end += 24
      (_x.battery_percentage, _x.battery_voltage, _x.pitch, _x.roll, _x.yaw, _x.heading,) = _struct_6f.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.drone = str[start:end].decode('utf-8')
      else:
        self.drone = str[start:end]
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_4f = struct.Struct("<4f")
_struct_6f = struct.Struct("<6f")
