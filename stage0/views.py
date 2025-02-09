from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import InfoSerializer
from datetime import datetime
import pytz

@api_view(['GET'])
def getdata(request):
        data = {
            "email": "onyishijamess@gmail.com",
            "current_datetime": datetime.now(pytz.utc).isoformat(),
            "github_url": "https://github.com/jamido1/HNG12Stage0.git"  
        }
        serializer = InfoSerializer(data)
        return Response(serializer.data)
