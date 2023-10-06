from src.database.projects import ProjectsORM
from src.controllers import Controllers


class ProjectController(Controllers):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_projects(self):
        with self.get_session() as session:
            projects = session.query(ProjectsORM).all()
            return [project.to_dict() for project in projects]

    def add_project(self, project_data: dict):
        with self.get_session() as session:
            # Create an instance of ProjectsORM using the project_data dictionary
            new_project = ProjectsORM(
                project_name=project_data.get('project_name'),
                introduction=project_data.get('introduction'),
                description=project_data.get('description'),
                image=project_data.get('image')  # Assuming 'image' is a key in project_data
            )

            # Add the new project to the session
            session.add(new_project)

            # Commit the changes to the database
            session.commit()
            return True

    def delete_project(self, _id: int):
        with self.get_session() as session:
            # Query the project by its ID
            project_to_delete = session.query(ProjectsORM).filter_by(id=_id).first()

            if project_to_delete:
                # If the project exists, delete it
                session.delete(project_to_delete)
                session.commit()
                return True  # Return True to indicate successful deletion
            else:
                # If the project doesn't exist, return False to indicate failure
                return False
