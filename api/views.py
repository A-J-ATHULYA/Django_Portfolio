from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import View

# Create your views here.
class About(View):
    def get(self, request):
        data = {
            "id" : 1, 
            "full_name" : "A.J.Athulya",
            "title" : "Python Developer",
            "bio" : "B.tech graduate with strong passion in web development.",
            "email" : "ajathulya@gmail.com",
            "mobile" : "1223436570",
            "linkedin_URL" : "https://www.linkedin.com/in/a-j-athulya-044866291/",
            "git_hub_Url" : "https://github.com/A-J-ATHULYA"
        }
        return JsonResponse(data)
    
class Education(View):
    def get(self, request):
        data = {
            "id" : 1, 
            "Institution" : "College of Engineering and management Punnapra",
            "University" : "KTU",
            "Location" : "Punnapra",
            "Qualification" : "B.Tech Computer Science",
            "Start Year" : "2022",
            "End Year" : "2026",
            "CGPA" : "6.87",
            "Description" : "Computer Science Engineer with strong passion for coding, debugging, testing, wed development ."
        }
        return JsonResponse(data)
    
class Project(View):
    def get(self, request):
        data = [
            {
                "id" : 1, 
                "Title" : "DDOS detection using AI",
                "Short Description" : "DDOS attack detection",
                "Long Description" : "DDOS live attack is dectected by using DL, ML mode and simulated environment is created for attack detection and attack classification ",
                "Technologies" : ["python", "flask", "HTML", "CS", "JS"],
                "Live URL" : "https://example.com/ecommerce",
                "GitHub URl" : "https://github.com/A-J-ATHULYA",
                "Image URL" : "https://example.com/images/ddos.jpg",
                "Featured" : True
            },
            {
                "id": 2,
                "Title": "E-Commerce Website",
                "Short Description": "A responsive online shopping website.",
                "Long Description": "An e-commerce website where users can browse products, view product details, add items to a cart, and place orders.",
                "Technologies" : ["python", "flask", "HTML", "CS", "JS"],
                "Live URL": "https://example.com/ecommerce",
                "GitHub URL": "https://github.com/example/ecommerce",
                "Image URL": "https://example.com/images/ecommerce.jpg",
                "Featured": True
                
            },
            {
                "id": 3,
                "Title": "Weather Monitoring System",
                "Short Description": "A web application for monitoring real-time weather conditions.",
                "Long Description": "A weather monitoring application that provides users with current temperature, humidity, wind speed, weather conditions, and other weather information for different locations.",
                "Technologies" : ["python", "flask", "HTML", "CS", "JS"],
                "Live URL": "https://example.com/weather-monitoring",
                "GitHub URL": "https://github.com/example/weather-monitoring",
                "Image URL": "https://example.com/images/weather-monitoring.jpg",
                "Featured": False  
            }
        ]
        return JsonResponse(data, safe=False)