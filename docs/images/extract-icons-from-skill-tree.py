from PIL import Image
import os


INPUT_IMAGE_FILE = "WakerSkillTree.webp"
START_OFFSET = (62, 6)
STRIDE = (181, 244)
ICON_SIZE = (48, 48)
OUTPUT_DIR = "skill-icons"

skill_icons: dict[str, tuple[int, int]] = {
    "Harmonizer Focus": (0, 0),
    "Retro Friends Rescue": (2, 0),
    "Welfare Management": (3, 0),
    "Resta Effect Continuance": (4, 0),
    "Lucky Sign": (5, 0),
    "Familiar Harmony": (0, 1),
    "Harmonizer Focus Extra": (1, 1),
    "Treble Clef Marking": (2, 1),
    "Marmelo Strike": (3, 1),
    "Call Again PP Preservation": (0, 2),
    "Familiar Harmony Marking Clef": (1, 2),
    "Treble Clef Ignition": (2, 2),
    "Hot Marmelo Parry": (3, 2),
    "Marmelo Strike Tracing": (4, 2),
    "Marmelo Patience": (5, 2),
    "Familiar Harmony Marmelo+": (1, 3),
    "Familiar Support": (2, 3),
    "Hot Marmelo Parry Short Cooldown": (3, 3),
    "Harmonizer Parry Counter": (4, 3),
    "Linear Drive": (5, 3),
    "Marmelo Support": (1, 4),
    "Familiar Support Amplifier": (2, 4),
    "Harmonizer Parry PP Gain": (4, 4),
    "Linear Drive Encore": (5, 4),
}


def join_words(s: str) -> str:
    return "".join(word for word in s.split())


def compute_offset(t: tuple[int, int]) -> tuple[int, int]:
    return (START_OFFSET[0] + t[0] * STRIDE[0], START_OFFSET[1] + t[1] * STRIDE[1])


def compute_bbox(t: tuple[int, int]) -> tuple[int, int, int, int]:
    start = compute_offset(t)
    return (start[0], start[1], start[0] + ICON_SIZE[0], start[1] + ICON_SIZE[1])


def extract_icons() -> None:
    """
    Extracts skill icons from the input image and saves them as WebP files.
    """
    try:
        # Check if the input image file exists.
        if not os.path.exists(INPUT_IMAGE_FILE):
            print(f"Error: Input file '{INPUT_IMAGE_FILE}' not found.")
            return

        # Open the original skill tree image.
        with Image.open(INPUT_IMAGE_FILE) as img:
            # Create the output directory if it doesn't exist.
            os.makedirs(OUTPUT_DIR, exist_ok=True)
            print(f"Saving icons to directory: '{OUTPUT_DIR}'")

            # Iterate through each skill and its coordinates.
            for skill_name, loc in skill_icons.items():
                # Define the bounding box for cropping.
                # The format is (left, upper, right, lower).
                bbox = compute_bbox(loc)

                # Crop the icon from the image.
                icon = img.crop(bbox)

                # Generate the PascalCase filename.
                filename = join_words(skill_name) + ".webp"
                file_path = os.path.join(OUTPUT_DIR, filename)

                # Save the cropped icon as a WebP file.
                icon.save(file_path, "WEBP", lossless=True)
                print(f"Successfully saved {filename}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    extract_icons()
