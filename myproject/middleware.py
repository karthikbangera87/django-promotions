from myapp.models import myapp 

class ReferMiddleware():
	def process_request(self, request):
		reference_id = request.GET.get("ref","")
		try:
			join_obj = myapp.objects.get(ref_id = reference_id)

		except:
			join_obj = None

		if join_obj:
			request.session['join_id'] = join_obj.id