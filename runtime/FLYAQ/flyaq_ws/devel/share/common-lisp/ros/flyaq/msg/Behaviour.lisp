; Auto-generated. Do not edit!


(cl:in-package flyaq-msg)


;//! \htmlinclude Behaviour.msg.html

(cl:defclass <Behaviour> (roslisp-msg-protocol:ros-message)
  ((name
    :reader name
    :initarg :name
    :type cl:string
    :initform "")
   (crs
    :reader crs
    :initarg :crs
    :type cl:string
    :initform "")
   (drones
    :reader drones
    :initarg :drones
    :type (cl:vector flyaq-msg:Drone)
   :initform (cl:make-array 0 :element-type 'flyaq-msg:Drone :initial-element (cl:make-instance 'flyaq-msg:Drone))))
)

(cl:defclass Behaviour (<Behaviour>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Behaviour>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Behaviour)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name flyaq-msg:<Behaviour> is deprecated: use flyaq-msg:Behaviour instead.")))

(cl:ensure-generic-function 'name-val :lambda-list '(m))
(cl:defmethod name-val ((m <Behaviour>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader flyaq-msg:name-val is deprecated.  Use flyaq-msg:name instead.")
  (name m))

(cl:ensure-generic-function 'crs-val :lambda-list '(m))
(cl:defmethod crs-val ((m <Behaviour>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader flyaq-msg:crs-val is deprecated.  Use flyaq-msg:crs instead.")
  (crs m))

(cl:ensure-generic-function 'drones-val :lambda-list '(m))
(cl:defmethod drones-val ((m <Behaviour>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader flyaq-msg:drones-val is deprecated.  Use flyaq-msg:drones instead.")
  (drones m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Behaviour>) ostream)
  "Serializes a message object of type '<Behaviour>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'name))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'name))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'crs))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'crs))
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'drones))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (roslisp-msg-protocol:serialize ele ostream))
   (cl:slot-value msg 'drones))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Behaviour>) istream)
  "Deserializes a message object of type '<Behaviour>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'name) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'name) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'crs) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'crs) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'drones) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'drones)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:aref vals i) (cl:make-instance 'flyaq-msg:Drone))
  (roslisp-msg-protocol:deserialize (cl:aref vals i) istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Behaviour>)))
  "Returns string type for a message object of type '<Behaviour>"
  "flyaq/Behaviour")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Behaviour)))
  "Returns string type for a message object of type 'Behaviour"
  "flyaq/Behaviour")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Behaviour>)))
  "Returns md5sum for a message object of type '<Behaviour>"
  "9b9d03cec42c32ed5c6a48197516edf1")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Behaviour)))
  "Returns md5sum for a message object of type 'Behaviour"
  "9b9d03cec42c32ed5c6a48197516edf1")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Behaviour>)))
  "Returns full string definition for message of type '<Behaviour>"
  (cl:format cl:nil "string name
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Behaviour)))
  "Returns full string definition for message of type 'Behaviour"
  (cl:format cl:nil "string name
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Behaviour>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'name))
     4 (cl:length (cl:slot-value msg 'crs))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'drones) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ (roslisp-msg-protocol:serialization-length ele))))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Behaviour>))
  "Converts a ROS message object to a list"
  (cl:list 'Behaviour
    (cl:cons ':name (name msg))
    (cl:cons ':crs (crs msg))
    (cl:cons ':drones (drones msg))
))