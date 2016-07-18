from django.http import HttpResponse, HttpResponseRedirect
from .models import Story, Annotator, Annotation, Label, Complete
from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt
from django.core.urlresolvers import reverse
import datetime
import re

@csrf_exempt
def index(request, username):
	user = None
	if Annotator.objects.filter(username = username).exists():
		user = Annotator.objects.get(username = username)
	else:
		error = {'error':'The url you input is not correct, please double check!'}
		return render(request, 'annot/error.html', error)
	user_id = user.pk
	time = datetime.datetime.now()
	complete_stories = []
	uncomplete_stories = []
	all_stories = Story.objects.all()
	if Complete.objects.filter(annotator=user).exists():
		complete_stories = [complete.story for complete in Complete.objects.filter(annotator=user)]
	if len(complete_stories) == 0:
		uncomplete_stories = all_stories
	else:
		uncomplete_stories = [story for story in all_stories if story not in complete_stories]
	if len(uncomplete_stories) == 0: ##finshed all stories
		story = complete_stories[0]
	else:
		story = uncomplete_stories[0]

	if len(request.POST) != 0:
		story = Story.objects.get(pk=request.POST.get('story_id'))
		if 'delete' in request.POST:
			annotation=Annotation.objects.get(pk=request.POST.get('delete'))
			annotation.delete()
		elif 'complete' in request.POST:
			if Complete.objects.filter(story=story, annotator=user).exists():
				complete = Complete.objects.get(story=story, annotator=user)
				complete.time = time
				complete.save()
			else:
				complete = Complete(story = story, annotator=user, time=time)
				complete.save()
			##update complete_stories list and uncomplete_stories list	
			complete_stories = [complete.story for complete in Complete.objects.filter(annotator=user)]
			uncomplete_stories = [story for story in all_stories if story not in complete_stories]
			if len(uncomplete_stories) == 0: ##finshed all stories
				story = complete_stories[0]
			else:
				story = uncomplete_stories[0]
		elif 'uncomplete' in request.POST:
			if Complete.objects.filter(story=story, annotator=user).exists():
				complete = Complete.objects.get(story=story, annotator=user)
				complete.delete()
			##update complete_stories list and uncomplete_stories list	
			complete_stories = [complete.story for complete in Complete.objects.filter(annotator=user)]
			uncomplete_stories = [story for story in all_stories if story not in complete_stories]
			if len(uncomplete_stories) == 0: ##finshed all stories
				story = complete_stories[0]
			else:
				story = uncomplete_stories[0]
		elif 'uncomplete_name' in request.POST:  ##go to an uncomplete story
			story = Story.objects.get(name=request.POST.get('uncomplete_name'))
		elif 'complete_name' in request.POST:  ##go to a complete story
			story = Story.objects.get(name=request.POST.get('complete_name'))
		else:			
			selectedText = request.POST.get('selectedText')
			label = request.POST.get('label')
			label_instance = Label.objects.get(name=label)
			start = request.POST.get('start')
			end = request.POST.get('end')
			story_id = story.pk
			annotation = Annotation(sentences=selectedText, time=time, story=story, annotator=user, label=label_instance, start=start, end=end)
			annotation.save()
			# return HttpResponseRedirect('')
		
	annotation_colors = {}
	annotation_list = Annotation.objects.filter(annotator = user_id, story=story).order_by('-time')
	for annotation in annotation_list:
		annotation_colors[annotation.start] = annotation.label.topclass.color

	if Complete.objects.filter(story=story, annotator=user).exists():
		completed = 'Completed'
	else:
		completed = 'Uncompleted'

	# story.content = story.content.replace('\n', '')
	# story.content = re.sub('\n+','',story.content)
	# print story.content

	# paragraphs = story.content.split('\n')  ##Separate paragraphs
	# paragraphs = ['<p>' + para + '</p>' for para in paragraphs]
	# paragraphs = ''.join(paragraphs)
	# story.content = paragraphs
	# print story.content
	context = {'story': story,
				'annotation_list': annotation_list,
				'annotation_colors': annotation_colors,
				'complete_stories': complete_stories,
				'uncomplete_stories': uncomplete_stories,
				'completed': completed
			}
	return render(request, 'annot/index.html', context)	