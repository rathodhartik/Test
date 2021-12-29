from copy import error
from rest_framework import status

from app import serializers







OK = status.HTTP_200_OK
CREATED = status.HTTP_201_CREATED
BAD_REQUEST =status.HTTP_400_BAD_REQUEST
NO_CONTENT =status.HTTP_204_NO_CONTENT





def success_added(message,data):
    msg={"code":CREATED,
             "message":message,
             "data":data
        
    }
    return msg

def data_fail(message,data):
    msg={"code":BAD_REQUEST,
         "message":message,
         "data":data
         }
    return msg


def update_data(message,data):
    msg={"code":OK,
             "message":message,
             "data":data
        
    }
    return msg

def deleted_data(message):
    msg={"code":NO_CONTENT,
             "message":message,
    }
    return msg
