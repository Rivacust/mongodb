from pymongo import MongoClient
from bson.objectid import ObjectId


client = MongoClient("mongodb+srv://Riva:qwe123@cluster0.a85vi.mongodb.net/",tlsAllowInvalidCertificates=True)
db = client["ytmanager"]
Video_collection = db["videos"]

def add_video(name, time):
    Video_collection.insert_one({"name": name, "time": time})

def update_video(Videoid, new_name, new_time):
    try:
        Video_collection.update_one({'_id': ObjectId(Videoid)}, {"$set": {"name": new_name, "time": new_time}})
    except Exception as e:
        print("Error updating video:", e)

def delete_video(Videoid):
    try:
        Video_collection.delete_one({"_id": ObjectId(Videoid)})
    except Exception as e:
        print("Error deleting video:", e)

def list_videos():
    for video in Video_collection.find():
        print(f"ID: {video['_id']}, Name: {video['name']}, Time: {video['time']}")

def main():
    while True:
        try:
            print("\nYT App")
            print("1. List all videos")
            print("2. Add new video")
            print("3. Update video")
            print("4. Delete video")
            print("5. Exit")
            
            choice = input("Enter your choice: ").strip()
            
            if choice == '1':
                list_videos()
            elif choice == '2':
                name = input("Enter video name: ").strip()
                time = input("Enter video time: ").strip()
                add_video(name, time)
                print("Video added successfully.")
            elif choice == '3':
                Videoid = input("Enter video ID: ").strip()
                new_name = input("Enter updated video name: ").strip()
                new_time = input("Enter updated time: ").strip()
                update_video(Videoid, new_name, new_time)
                print("Video updated successfully.")
            elif choice == '4':
                Videoid = input("Enter video ID: ").strip()
                delete_video(Videoid)
                print("Video deleted successfully.")
            elif choice == '5':
                print("Exiting...")
                break
            else:
                print("Invalid choice, please try again.")

        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
