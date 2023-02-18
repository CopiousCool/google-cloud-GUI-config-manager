import os
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import simpledialog
from google.cloud import compute_v1
from google.oauth2 import service_account
import logging


class GCloudGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Google Cloud Manager")
        self.geometry("600x400")

        # Configure logging
        logging.basicConfig(filename="gcloud_gui.log", level=logging.DEBUG,
                            format="%(asctime)s:%(levelname)s:%(message)s")

        # Check if the credentials file exists
        credentials_file = "path/to/credentials.json"
        while not os.path.exists(credentials_file):
            # Show a dialog to select the credentials file
            credentials_file = simpledialog.askstring("Credentials file", "Please enter the path to the credentials file:")
            if not credentials_file:
                # If the user did not select a credentials file, close the application
                self.destroy()
                return

            try:
                # Load the service account credentials
                self.credentials = service_account.Credentials.from_service_account_file(credentials_file)

                # Create the compute engine client
                self.compute_client = compute_v1.ComputeClient(credentials=self.credentials)

                # Create the UI
                self.create_ui()
            except Exception as e:
                # Show an error message if there was an error loading the credentials
                choice = messagebox.askretrycancel("Error", f"Error loading credentials: {e}\n\nPress Retry to select a different credentials file or Cancel to exit.")
                if not choice:
                    self.destroy()
                    return
                credentials_file = ""
        
        # Load the service account credentials
        self.credentials = service_account.Credentials.from_service_account_file(
            credentials_file)

        # Create the compute engine client
        self.compute_client = compute_v1.ComputeClient(credentials=self.credentials)

        # Create the UI
        self.create_ui()


    def create_ui(self):
        # Create the main frame
        self.main_frame = tk.Frame(self)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Create the tabs
        self.tabs = ttk.Notebook(self.main_frame)
        self.tabs.pack(fill=tk.BOTH, expand=True)

        # Create the instances tab
        self.instances_frame = tk.Frame(self.tabs)
        self.tabs.add(self.instances_frame, text="Instances")
        self.instances = Instances(self.instances_frame, self.compute_client)

        # Create the clusters tab
        self.clusters_frame = tk.Frame(self.tabs)
        self.tabs.add(self.clusters_frame, text="Clusters")
        self.clusters = Clusters(self.clusters_frame, self.compute_client)


class Instances:
    def __init__(self, parent, compute_client):
        self.parent = parent
        self.compute_client = compute_client
        self.create_ui()

    def create_ui(self):
        # Create the instance frame
        self.instance_frame = tk.Frame(self.parent)
        self.instance_frame.pack(fill=tk.BOTH, expand=True)

        # Create the instance label
        instance_label = tk.Label(self.instance_frame, text="Instances")
        instance_label.pack()

        # Create the instance listbox
        self.instance_listbox = tk.Listbox(self.instance_frame, width=50)
        self.instance_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Create the instance scrollbar
        self.instance_scrollbar = tk.Scrollbar(self.instance_frame, orient=tk.VERTICAL)
        self.instance_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Configure the instance listbox to use the scrollbar
        self.instance_listbox.config(yscrollcommand=self.instance_scrollbar.set)
        self.instance_scrollbar.config(command=self.instance_listbox.yview)

        # Load the instances
        self.load_instances()

    def load_instances(self):
        try:
            # Get the list of instances
            instances = self.compute_client.list_instances()

            # Populate the instance listbox
            for instance in instances:
                self.instance_listbox.insert(tk.END, instance.name)

        except Exception as e:
            # Log the error message
            logging.error(f"Error loading instances: {e}")

            # Show an error message
            messagebox.showerror("Error", f"Error loading instances: {e}") 


class Clusters:

    def init(self, parent, compute_client):
        self.parent = parent
        self.compute_client = compute_client
        self.create_ui()

    def create_ui(self):
        # Create the cluster frame
        self.cluster_frame = tk.Frame(self.parent)
        self.cluster_frame.pack(fill=tk.BOTH, expand=True)

        # Create the cluster label
        cluster_label = tk.Label(self.cluster_frame, text="Clusters")
        cluster_label.pack()

        # Create the cluster listbox
        self.cluster_listbox = tk.Listbox(self.cluster_frame, width=50)
        self.cluster_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Create the cluster scrollbar
        self.cluster_scrollbar = tk.Scrollbar(self.cluster_frame, orient=tk.VERTICAL)
        self.cluster_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Configure the cluster listbox to use the scrollbar
        self.cluster_listbox.config(yscrollcommand=self.cluster_scrollbar.set)
        self.cluster_scrollbar.config(command=self.cluster_listbox.yview)

        # Load the clusters
        self.load_clusters()


    def load_clusters(self):
        try:
            # Get the list of clusters
            clusters = self.compute_client.list_clusters()

            # Populate the cluster listbox
            for cluster in clusters:
                self.cluster_listbox.insert(tk.END, cluster.name)

        except Exception as e:
            # Log the error message
            logging.error(f"Error loading clusters: {e}")

            # Show an error message
            messagebox.showerror("Error", f"Error loading clusters: {e}") 


if __name__ == "__main__":
    GCloudGUI().mainloop()
