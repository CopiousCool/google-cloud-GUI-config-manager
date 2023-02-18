# google-cloud-GUI-config-manager

This code is a Python program for a graphical user interface (GUI) to manage resources in Google Cloud. The GUI is built using the tkinter library.

# Google Cloud GUI
The Google Cloud GUI is a graphical user interface for managing instances and clusters in Google Cloud Platform. It uses the Google Cloud Python SDK to communicate with the Google Cloud APIs.

# Requirements

Python 3.x
Google Cloud SDK
Tkinter (included in standard library)

# Installation
Install Python 3.x: https://www.python.org/downloads/
Install the Google Cloud SDK: https://cloud.google.com/sdk/docs/install
Install the required Python packages: pip install google-cloud-compute google-auth tkinter
Download the Google Cloud GUI source code.

# Usage
Open a terminal window and navigate to the directory where the Google Cloud GUI source code is located.
Run the following command to start the application: python gcloud_gui.py

When prompted, enter the path to the JSON file containing the service account credentials for the Google Cloud project you want to manage. If you do not have a JSON file, follow the instructions at https://cloud.google.com/docs/authentication/getting-started to create one.
The Google Cloud GUI will open with two tabs: Instances and Clusters. Click on a tab to view and manage instances or clusters.

# Classes
# GCloudGUI
The GCloudGUI class is the main class of the application. It inherits from the tk.Tk class and provides the graphical user interface for managing instances and clusters in Google Cloud Platform.

Attributes
credentials: An instance of the google.auth.credentials.Credentials class containing the service account credentials for the Google Cloud project.
compute_client: An instance of the google.cloud.compute_v1.ComputeClient class for managing compute resources in the Google Cloud project.

Methods
__init__(self): Initializes the GCloudGUI object and creates the main window.
create_ui(self): Creates the user interface for the main window and adds the tabs for managing instances and clusters.


# Instances
The Instances class is a helper class for the GCloudGUI class. It creates the user interface for managing instances in Google Cloud Platform.

Attributes
parent: The parent frame of the instances tab.
compute_client: An instance of the google.cloud.compute_v1.ComputeClient class for managing compute resources in the Google Cloud project.
Methods
__init__(self, parent, compute_client): Initializes the Instances object and creates the user interface for managing instances.
create_ui(self): Creates the user interface for the instances tab.
load_instances(self): Loads the list of instances from the Google Cloud project and populates the instance listbox.

# Clusters
The Clusters class is a helper class for the GCloudGUI class. It creates the user interface for managing clusters in Google Cloud Platform.

Attributes
parent: The parent frame of the clusters tab.
compute_client: An instance of the google.cloud.compute_v1.ComputeClient class for managing compute resources in the Google Cloud project.
Methods
__init__(self, parent, compute_client): Initializes the Clusters object and creates the user interface for managing clusters.
create_ui(self): Creates the user interface for the clusters tab.
load_clusters(self): Loads the list of clusters from the Google Cloud project and populates the cluster listbox.


The program defines a GCloudGUI class that inherits from the tk.Tk class. The __init__ method of the GCloudGUI class sets the title and geometry of the main window. It then sets up logging to write debug information to a file, and checks if a credentials file exists. If the file does not exist, the program displays a dialog to prompt the user to select the credentials file. If the user cancels the dialog, the program terminates. If the user selects a file, the program attempts to load the service account credentials from the file, and creates a ComputeClient instance using the credentials. If there is an error loading the credentials, the program displays an error message and prompts the user to retry or cancel. If the user cancels, the program terminates. If the user retries, the program displays the credentials file dialog again.

The GCloudGUI class also defines a create_ui method that creates the main frame of the GUI and sets up two tabs, one for managing instances and one for managing clusters. Each tab is created by instantiating an Instances or Clusters object and passing in the parent frame and ComputeClient instance.

The Instances class manages the instances tab of the GUI. Its __init__ method receives a reference to the parent frame and the ComputeClient instance, and calls the create_ui method to create the instance frame, label, listbox, scrollbar, and load the list of instances. The create_ui method creates a frame to hold the instance-related GUI elements, creates a label to display the text "Instances", creates a listbox to display a list of instances, creates a scrollbar for the listbox, and configures the listbox to use the scrollbar. It also calls the load_instances method to populate the listbox with the names of instances in the project. The load_instances method calls the list_instances method of the ComputeClient instance to retrieve a list of instances, and populates the listbox with the names of the instances.

The Clusters class manages the clusters tab of the GUI. Its __init__ method receives a reference to the parent frame and the ComputeClient instance, and calls the create_ui method to create the cluster frame, label, listbox, scrollbar, and load the list of clusters. The create_ui method creates a frame to hold the cluster-related GUI elements, creates a label to display the text "Clusters", creates a listbox to display a list of clusters, creates a scrollbar for the listbox, and configures the listbox to use the scrollbar. It also calls the load_clusters method to populate the listbox with the names of clusters in the project. The load_clusters method calls the list_clusters method of the ComputeClient instance to retrieve a list of clusters, and populates the listbox with the names of the clusters.
