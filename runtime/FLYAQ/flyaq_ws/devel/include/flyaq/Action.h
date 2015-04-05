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
 * Auto-generated by genmsg_cpp from file /home/viki/Desktop/FLYAQ/flyaq_ws/src/flyaq/msg/Action.msg
 *
 */


#ifndef FLYAQ_MESSAGE_ACTION_H
#define FLYAQ_MESSAGE_ACTION_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <flyaq/Parameter.h>

namespace flyaq
{
template <class ContainerAllocator>
struct Action_
{
  typedef Action_<ContainerAllocator> Type;

  Action_()
    : name()
    , type(0)
    , action_name()
    , parameters()
    , slot_name()
    , receivers_name()  {
    }
  Action_(const ContainerAllocator& _alloc)
    : name(_alloc)
    , type(0)
    , action_name(_alloc)
    , parameters(_alloc)
    , slot_name(_alloc)
    , receivers_name(_alloc)  {
    }



   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _name_type;
  _name_type name;

   typedef int8_t _type_type;
  _type_type type;

   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _action_name_type;
  _action_name_type action_name;

   typedef std::vector< ::flyaq::Parameter_<ContainerAllocator> , typename ContainerAllocator::template rebind< ::flyaq::Parameter_<ContainerAllocator> >::other >  _parameters_type;
  _parameters_type parameters;

   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _slot_name_type;
  _slot_name_type slot_name;

   typedef std::vector<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > , typename ContainerAllocator::template rebind<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::other >  _receivers_name_type;
  _receivers_name_type receivers_name;


    enum { DEVICE = 0 };
     enum { FEEDBACK = 1 };
     enum { CHECK = 2 };
     enum { UNICAST_NOTIFY = 3 };
     enum { MULTICAST_NOTIFY = 4 };
     enum { BROADCAST_NOTIFY = 5 };
 

  typedef boost::shared_ptr< ::flyaq::Action_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::flyaq::Action_<ContainerAllocator> const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;

}; // struct Action_

typedef ::flyaq::Action_<std::allocator<void> > Action;

typedef boost::shared_ptr< ::flyaq::Action > ActionPtr;
typedef boost::shared_ptr< ::flyaq::Action const> ActionConstPtr;

// constants requiring out of line definition

   

   

   

   

   

   



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::flyaq::Action_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::flyaq::Action_<ContainerAllocator> >::stream(s, "", v);
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
struct IsFixedSize< ::flyaq::Action_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::flyaq::Action_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::flyaq::Action_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::flyaq::Action_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::flyaq::Action_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::flyaq::Action_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::flyaq::Action_<ContainerAllocator> >
{
  static const char* value()
  {
    return "58f0748716c1150e99fa89f4cf20c9b6";
  }

  static const char* value(const ::flyaq::Action_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x58f0748716c1150eULL;
  static const uint64_t static_value2 = 0x99fa89f4cf20c9b6ULL;
};

template<class ContainerAllocator>
struct DataType< ::flyaq::Action_<ContainerAllocator> >
{
  static const char* value()
  {
    return "flyaq/Action";
  }

  static const char* value(const ::flyaq::Action_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::flyaq::Action_<ContainerAllocator> >
{
  static const char* value()
  {
    return "string name\n\
int8 DEVICE = 0\n\
int8 FEEDBACK = 1\n\n\
int8 CHECK = 2\n\n\
int8 UNICAST_NOTIFY = 3\n\n\
int8 MULTICAST_NOTIFY = 4\n\n\
int8 BROADCAST_NOTIFY = 5\n\n\
int8 type # enumerate above\n\n\
string action_name # filled only in case of DeviceAction and Feedback\n\n\
Parameter[] parameters # filled only in case of DeviceAction and Feedback\n\n\
string slot_name # filled only in case of Notify (any kind) or CheckNotification\n\n\
string[] receivers_name # filled only in case of MulticastNotify or UnicastNotify\n\n\n\
================================================================================\n\
MSG: flyaq/Parameter\n\
string key\n\
string value\n\n\
";
  }

  static const char* value(const ::flyaq::Action_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::flyaq::Action_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.name);
      stream.next(m.type);
      stream.next(m.action_name);
      stream.next(m.parameters);
      stream.next(m.slot_name);
      stream.next(m.receivers_name);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER;
  }; // struct Action_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::flyaq::Action_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::flyaq::Action_<ContainerAllocator>& v)
  {
    s << indent << "name: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.name);
    s << indent << "type: ";
    Printer<int8_t>::stream(s, indent + "  ", v.type);
    s << indent << "action_name: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.action_name);
    s << indent << "parameters[]" << std::endl;
    for (size_t i = 0; i < v.parameters.size(); ++i)
    {
      s << indent << "  parameters[" << i << "]: ";
      s << std::endl;
      s << indent;
      Printer< ::flyaq::Parameter_<ContainerAllocator> >::stream(s, indent + "    ", v.parameters[i]);
    }
    s << indent << "slot_name: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.slot_name);
    s << indent << "receivers_name[]" << std::endl;
    for (size_t i = 0; i < v.receivers_name.size(); ++i)
    {
      s << indent << "  receivers_name[" << i << "]: ";
      Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.receivers_name[i]);
    }
  }
};

} // namespace message_operations
} // namespace ros

#endif // FLYAQ_MESSAGE_ACTION_H
