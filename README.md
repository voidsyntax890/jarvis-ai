# Jarvis AI - Voice Assistant

A Python-based voice-activated AI assistant inspired by Tony Stark's Jarvis. This assistant can perform various tasks including web browsing, playing music, fetching news, and engaging in conversations using OpenAI's GPT model.

## Features

- **Voice Recognition**: Responds to "Jarvis" wake word
- **Web Browsing**: Opens popular websites (Google, Facebook, YouTube, LinkedIn)
- **Music Player**: Plays songs from a predefined music library via YouTube
- **News Updates**: Fetches and reads latest news headlines
- **AI Conversations**: Powered by OpenAI GPT-3.5 for general queries
- **Text-to-Speech**: Two speech synthesis options available (pyttsx3 and gTTS)

## Prerequisites

- Python 3.7+
- Microphone access
- Internet connection
- OpenAI API key
- NewsAPI key

## Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/jarvis-ai.git
cd jarvis-ai
```

2. **Install required packages**
```bash
pip install speech_recognition
pip install webbrowser
pip install pyttsx3
pip install requests
pip install openai
pip install gtts
pip install pygame
pip install pocketsphinx
```

3. **Set up API Keys**
   - Get your OpenAI API key from [OpenAI Platform](https://platform.openai.com/)
   - Get your NewsAPI key from [NewsAPI](https://newsapi.org/)
   - Replace the placeholder API keys in the code with your actual keys

## Project Structure

```
jarvis-ai/
│
├── main.py              # Main application file
├── client.py            # OpenAI client test file
├── musicLibrary.py      # Music library with YouTube links
├── musicLibrary.txt     # Backup music library
├── main.txt             # Alternative main file with gTTS
└── README.md           # Project documentation
```

## Configuration

### API Keys Setup

1. **OpenAI API Key**: Replace `<Your Key Here>` in the `aiProcess()` function
2. **NewsAPI Key**: Replace `<Your Key Here>` in the `newsapi` variable

### Music Library

Add your favorite songs to `musicLibrary.py`:
```python
music = {
    "song_name": "youtube_url",
    "stealth": "https://www.youtube.com/watch?v=U47Tr9BB_wE",
    # Add more songs here
}
```

## Usage

1. **Run the application**
```bash
python main.py
```

2. **Wake up Jarvis**
   - Say "Jarvis" to activate the assistant
   - Wait for the "Ya" response

3. **Give commands**
   - "Open Google" - Opens Google in browser
   - "Open YouTube" - Opens YouTube in browser
   - "Play [song_name]" - Plays song from music library
   - "News" - Reads latest news headlines
   - Ask any general question for AI-powered responses

## Voice Commands

| Command | Action |
|---------|--------|
| "Open Google" | Opens Google.com |
| "Open Facebook" | Opens Facebook.com |
| "Open YouTube" | Opens YouTube.com |
| "Open LinkedIn" | Opens LinkedIn.com |
| "Play [song]" | Plays specified song from library |
| "News" | Reads latest Indian news headlines |
| Any other query | Processes through OpenAI GPT |

## Technical Details

### Speech Recognition
- Uses Google's speech recognition API
- Supports wake word detection
- Handles command processing with error handling

### Text-to-Speech Options
- **Option 1**: pyttsx3 (offline, faster)
- **Option 2**: gTTS with pygame (online, better quality)

### AI Integration
- OpenAI GPT-3.5-turbo model
- Configured as a virtual assistant
- Provides short, concise responses

## Important Security Notes

- **Never commit your API keys** to version control
- Use environment variables for API keys in production
- The current code contains placeholder keys - replace them with your own

## Troubleshooting

### Common Issues

1. **Speech Recognition Errors**
   - Ensure microphone permissions are granted
   - Check internet connection
   - Speak clearly and close to the microphone

2. **API Key Errors**
   - Verify your OpenAI API key is valid
   - Check your OpenAI account credits
   - Ensure NewsAPI key is active

3. **Audio Issues**
   - Install required audio libraries
   - Check system audio settings
   - For gTTS version, ensure pygame is properly installed

## Version History

- **v1.0**: Basic voice recognition and web browsing
- **v2.0**: Added music library and news features
- **v3.0**: Integrated OpenAI GPT for conversations
- **v4.0**: Added gTTS support for better speech quality

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

This project is for educational purposes. Ensure you comply with:
- OpenAI's usage policies
- NewsAPI terms of service
- YouTube's terms of service for automated access
- Local laws regarding voice recording and processing

## Acknowledgments

- OpenAI for GPT API
- Google for Speech Recognition API
- NewsAPI for news data
- Python community for excellent libraries

---

**Made with ❤️ by [ANIRBAN BHATTACHARYYA]**