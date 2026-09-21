"""Unit tests for the emotion_detection module."""

import unittest
from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """Test cases for emotion_detector function."""

    def test_joy_for_glad_statement(self):
        """Test that joy is the dominant emotion for a glad statement."""
        result = emotion_detector('I am glad this happened')
        self.assertEqual(result['dominant_emotion'], 'joy')

    def test_anger_for_mad_statement(self):
        """Test that anger is the dominant emotion for a mad statement."""
        result = emotion_detector('I am really mad about this')
        self.assertEqual(result['dominant_emotion'], 'anger')

    def test_disgust_for_disgusted_statement(self):
        """Test that disgust is the dominant emotion for a disgusted statement."""
        result = emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual(result['dominant_emotion'], 'disgust')

    def test_sadness_for_sad_statement(self):
        """Test that sadness is the dominant emotion for a sad statement."""
        result = emotion_detector('I am so sad about this')
        self.assertEqual(result['dominant_emotion'], 'sadness')

    def test_fear_for_afraid_statement(self):
        """Test that fear is the dominant emotion for a fearful statement."""
        result = emotion_detector('I am really afraid that this will happen')
        self.assertEqual(result['dominant_emotion'], 'fear')


if __name__ == '__main__':
    unittest.main()

