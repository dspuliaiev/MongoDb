from typing import List
from models import Author, Quote


def find_by_tag(tag: str) -> List[str]:
    print(f"Find by tag: {tag}")
    quotes = Quote.objects(tags__iregex=tag)
    result = [q.quote for q in quotes]
    return result


def find_by_author(author: str) -> List[str]:
    print(f"Find by author: {author}")
    authors = Author.objects(fullname__iregex=author)
    result = {}
    for a in authors:
        quotes = Quote.objects(author=a)
        result[a.fullname] = [q.quote for q in quotes]
    return result


def find_by_tags(tags: str) -> List[str]:
    tag_list = tags.split(',')
    print(f"Find by tags: {tag_list}")
    quotes = Quote.objects(tags__in=tag_list)
    result = [q.quote for q in quotes]
    return result


def main():
    while True:
        print("Welcome to Finder Bot!")
        print("Commands:")
        print("name:<author_name> - Find quotes by author name")
        print("tag:<tag_name> - Find quotes by tag")
        print("tags:<tag1>,<tag2>,... - Find quotes by multiple tags")
        print("exit - Exit the program")

        command = input("Enter command: ")

        if command.startswith("name:"):
            author_name = command.split(":")[1].strip()
            quotes = find_by_author(author_name)
            if quotes:
                print("Quotes found:")
                for author, quotes in quotes.items():
                    print(f"By {author}:")
                    for quote in quotes:
                        print(quote)
            else:
                print("No quotes found for this author.")

        elif command.startswith("tag:"):
            tag_name = command.split(":")[1].strip()
            quotes = find_by_tag(tag_name)
            if quotes:
                print("Quotes found:")
                for quote in quotes:
                    print(quote)
            else:
                print("No quotes found for this tag.")

        elif command.startswith("tags:"):
            tag_names = command.split(":")[1].strip()
            quotes = find_by_tags(tag_names)
            if quotes:
                print("Quotes found:")
                for quote in quotes:
                    print(quote)
            else:
                print("No quotes found for these tags.")

        elif command == "exit":
            print("Exiting...")
            break

        else:
            print("Invalid command. Please enter a valid command.")


if __name__ == '__main__':
    main()