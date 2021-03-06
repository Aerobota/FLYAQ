/* Software License Agreement (BSD License)
 *
 * Copyright (c) 2011, Willow Garage, Inc.
 * All rights reserved.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions
 * are met:
 *
 *  * Redistributions of source code must retain the above copyright
 *    notice, this list of conditions and the following disclaimer.
 *  * Redistributions in binary form must reproduce the above
 *    copyright notice, this list of conditions and the following
 *    disclaimer in the documentation and/or other materials provided
 *    with the distribution.
 *  * Neither the name of Willow Garage, Inc. nor the names of its
 *    contributors may be used to endorse or promote products derived
 *    from this software without specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
 * "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
 * LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
 * FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
 * COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
 * INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
 * BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
 * LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
 * CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
 * LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
 * ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
 * POSSIBILITY OF SUCH DAMAGE.
 *
 * Auto-generated by genmsg_cpp from file /home/viki/Desktop/FLYAQ/flyaq_ws/src/flyaq/msg/Feedback.msg
 *
 */


#ifndef FLYAQ_MESSAGE_FEEDBACK_H
#define FLYAQ_MESSAGE_FEEDBACK_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace flyaq
{
template <class ContainerAllocator>
struct Feedback_
{
  typedef Feedback_<ContainerAllocator> Type;

  Feedback_()
    : latitude(0.0)
    , longitude(0.0)
    , altitude(0.0)
    , speed(0.0)
    , status()
    , msg()
    , battery_percentage(0.0)
    , battery_voltage(0.0)
    , pitch(0.0)
    , roll(0.0)
    , yaw(0.0)
    , heading(0.0)
    , drone()  {
    }
  Feedback_(const ContainerAllocator& _alloc)
    : latitude(0.0)
    , longitude(0.0)
    , altitude(0.0)
    , speed(0.0)
    , status(_alloc)
    , msg(_alloc)
    , battery_percentage(0.0)
    , battery_voltage(0.0)
    , pitch(0.0)
    , roll(0.0)
    , yaw(0.0)
    , heading(0.0)
    , drone(_alloc)  {
    }



   typedef float _latitude_type;
  _latitude_type latitude;

   typedef float _longitude_type;
  _longitude_type longitude;

   typedef float _altitude_type;
  _altitude_type altitude;

   typedef float _speed_type;
  _speed_type speed;

   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _status_type;
  _status_type status;

   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _msg_type;
  _msg_type msg;

   typedef float _battery_percentage_type;
  _battery_percentage_type battery_percentage;

   typedef float _battery_voltage_type;
  _battery_voltage_type battery_voltage;

   typedef float _pitch_type;
  _pitch_type pitch;

   typedef float _roll_type;
  _roll_type roll;

   typedef float _yaw_type;
  _yaw_type yaw;

   typedef float _heading_type;
  _heading_type heading;

   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _drone_type;
  _drone_type drone;




  typedef boost::shared_ptr< ::flyaq::Feedback_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::flyaq::Feedback_<ContainerAllocator> const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;

}; // struct Feedback_

typedef ::flyaq::Feedback_<std::allocator<void> > Feedback;

typedef boost::shared_ptr< ::flyaq::Feedback > FeedbackPtr;
typedef boost::shared_ptr< ::flyaq::Feedback const> FeedbackConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::flyaq::Feedback_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::flyaq::Feedback_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace flyaq

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': False, 'IsMessage': True, 'HasHeader': False}
// {'std_msgs': ['/opt/ros/groovy/share/std_msgs/msg'], 'flyaq': ['/home/viki/Desktop/FLYAQ/flyaq_ws/src/flyaq/msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::flyaq::Feedback_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::flyaq::Feedback_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::flyaq::Feedback_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::flyaq::Feedback_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::flyaq::Feedback_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::flyaq::Feedback_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::flyaq::Feedback_<ContainerAllocator> >
{
  static const char* value()
  {
    return "0e4c4d5eb3b453fc011856d2f2bcfc94";
  }

  static const char* value(const ::flyaq::Feedback_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x0e4c4d5eb3b453fcULL;
  static const uint64_t static_value2 = 0x011856d2f2bcfc94ULL;
};

template<class ContainerAllocator>
struct DataType< ::flyaq::Feedback_<ContainerAllocator> >
{
  static const char* value()
  {
    return "flyaq/Feedback";
  }

  static const char* value(const ::flyaq::Feedback_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::flyaq::Feedback_<ContainerAllocator> >
{
  static const char* value()
  {
    return "float32 latitude\n\
float32 longitude\n\
float32 altitude\n\
float32 speed\n\
string status\n\
string msg \n\
float32 battery_percentage\n\
float32 battery_voltage\n\
float32 pitch\n\
float32 roll\n\
float32 yaw\n\
float32 heading\n\
string drone # the drone providing the feedback\n\n\
";
  }

  static const char* value(const ::flyaq::Feedback_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::flyaq::Feedback_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.latitude);
      stream.next(m.longitude);
      stream.next(m.altitude);
      stream.next(m.speed);
      stream.next(m.status);
      stream.next(m.msg);
      stream.next(m.battery_percentage);
      stream.next(m.battery_voltage);
      stream.next(m.pitch);
      stream.next(m.roll);
      stream.next(m.yaw);
      stream.next(m.heading);
      stream.next(m.drone);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER;
  }; // struct Feedback_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::flyaq::Feedback_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::flyaq::Feedback_<ContainerAllocator>& v)
  {
    s << indent << "latitude: ";
    Printer<float>::stream(s, indent + "  ", v.latitude);
    s << indent << "longitude: ";
    Printer<float>::stream(s, indent + "  ", v.longitude);
    s << indent << "altitude: ";
    Printer<float>::stream(s, indent + "  ", v.altitude);
    s << indent << "speed: ";
    Printer<float>::stream(s, indent + "  ", v.speed);
    s << indent << "status: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.status);
    s << indent << "msg: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.msg);
    s << indent << "battery_percentage: ";
    Printer<float>::stream(s, indent + "  ", v.battery_percentage);
    s << indent << "battery_voltage: ";
    Printer<float>::stream(s, indent + "  ", v.battery_voltage);
    s << indent << "pitch: ";
    Printer<float>::stream(s, indent + "  ", v.pitch);
    s << indent << "roll: ";
    Printer<float>::stream(s, indent + "  ", v.roll);
    s << indent << "yaw: ";
    Printer<float>::stream(s, indent + "  ", v.yaw);
    s << indent << "heading: ";
    Printer<float>::stream(s, indent + "  ", v.heading);
    s << indent << "drone: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.drone);
  }
};

} // namespace message_operations
} // namespace ros

#endif // FLYAQ_MESSAGE_FEEDBACK_H
