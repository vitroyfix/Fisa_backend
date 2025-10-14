Fisa Backend Project

This README documents the Fisa Backend, built with Django and Django REST Framework (DRF). It outlines the project structure, API endpoints, workflow, and current program.


1. Project Overview

Fisa Backend is designed to manage:

* Events and council participation
* Student and attendee information
* Non-member records
* Media uploads
* Admin management

Key Features:

* Event management with participation tracking
* Detailed models for students, council members, and attendees
* Media handling for uploads and serving files
* DRF-based CRUD API endpoints
* Admin panel for easy data management

2. API Endpoints

The URL configuration in `Fisa_backend.urls` exposes the following endpoints:

 
 `api/admin/`       Access Django admin panel to manage models.              
`api/admissions/` CRUD operations for student admissions data.             
 `api/attendees/`   Manage event attendees and their registration details.   
 `api/council/`     Manage council members and event participation.          
  `api/media/`      Handle media uploads and serve uploaded files.           
 `api/events/`      CRUD operations for events and participation tracking.   
 `api/nonmembers/`  Manage non-member records for events and communications. 
 `api/students/`    Student-specific operations, separate from admissions.   
 `uploads/<path>`   Serve uploaded files from the server.                    

3. How the Project Works

 3.1 Models

* Event & CouncilEventParticipation**: Tracks events and council member involvement.
* Admissions, Students, Attendees, NonMembers**: Manage different user types and their data.
* Media Models**: Handle file uploads and storage.

 3.2 API Structure

* Each app has its own serializers, views, and URLs.
* DRF manages CRUD operations and data validation.
* Endpoints are tested locally using Postman to ensure correct responses.

 3.3 Admin Panel

* Provides a UI for managing all models.
* Allows quick verification of relationships and uploaded files.

 3.4 Media & File Handling

* Uploads are served via `/uploads/<path>`.
* Configured for development and can be adapted for production storage.

4. Challenges & Solutions

1. Serializing ManyToMany Relationships

   * olution:Used nested serializers in DRF to correctly display related data.

2. Handling JSONField for Lists

   * Solution:Used default lists and validated input/output via Postman.

3. Local Testing & Configuration Issues

   * Solution: Configured local server, set proper CORS headers, and verified all routes.



5. Future Plans

* Implement authentication and permissions for secure API access.
* Expand endpoints for reporting and analytics.
* Improve admin customization for better usability.
* Complete frontend integration and test end-to-end functionality.

---

 6. Notes on Debugging & 404 Pages

* If you visit the root URL `/` without a defined path, Django shows a **404 page** because the empty path does not match any URL patterns.
* This behavior occurs with `DEBUG=True`. In production, set `DEBUG=False` for a standard 404 page.

Current URL Patterns:

api/admin/
api/admissions/
api/attendees/
api/council/
api/media/
api/events/
api/nonmembers/
api/students/
uploads/(?P<path>.*)$


Reflection:
The project is now well-structured and functional. The backend APIs cover all major functionalities, and the admin panel provides robust management. Testing and debugging have ensured a stable foundation for frontend integration.


