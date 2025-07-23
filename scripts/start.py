#!/usr/bin/env python3
"""
Universal startup script for Cyberpunk Task Board
Works on Windows, macOS, and Linux
"""

import os
import sys
import subprocess
import time
import platform
import threading
import webbrowser
from pathlib import Path

def check_python_version():
    """Check if Python 3.8+ is available"""
    if sys.version_info < (3, 8):
        print("❌ Python 3.8 or higher is required")
        sys.exit(1)
    print(f"✅ Python {sys.version.split()[0]} detected")

def setup_virtual_environment():
    """Create and setup virtual environment"""
    venv_path = Path("venv")
    
    if not venv_path.exists():
        print("📦 Creating virtual environment...")
        subprocess.run([sys.executable, "-m", "venv", "venv"], check=True)
        print("✅ Virtual environment created")
    else:
        print("✅ Virtual environment already exists")
    
    # Get the correct paths for different operating systems
    if platform.system() == "Windows":
        python_path = venv_path / "Scripts" / "python.exe"
        pip_path = venv_path / "Scripts" / "pip.exe"
    else:
        python_path = venv_path / "bin" / "python"
        pip_path = venv_path / "bin" / "pip"
    
    return python_path, pip_path

def install_dependencies(pip_path):
    """Install required dependencies"""
    print("📥 Installing dependencies...")
    try:
        subprocess.run([str(pip_path), "install", "-r", "requirements.txt"], check=True)
        # Install additional required dependency
        subprocess.run([str(pip_path), "install", "python-multipart"], check=True)
        print("✅ Dependencies installed successfully")
    except subprocess.CalledProcessError:
        print("❌ Failed to install dependencies")
        sys.exit(1)

def start_fastapi_server(python_path):
    """Start FastAPI server in a separate thread"""
    def run_fastapi():
        env = os.environ.copy()
        subprocess.run([
            str(python_path), "-m", "uvicorn", 
            "backend.main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"
        ], env=env)
    
    thread = threading.Thread(target=run_fastapi, daemon=True)
    thread.start()
    return thread

def start_flask_server(python_path):
    """Start Flask server"""
    env = os.environ.copy()
    env["FASTAPI_URL"] = "http://localhost:8000"
    
    subprocess.run([str(python_path), "-m", "frontend.app"], env=env)

def wait_for_server(url, timeout=30):
    """Wait for server to be ready"""
    import urllib.request
    import urllib.error
    
    for _ in range(timeout):
        try:
            urllib.request.urlopen(url, timeout=1)
            return True
        except (urllib.error.URLError, ConnectionError):
            time.sleep(1)
    return False

def main():
    """Main startup function"""
    print("🚀 Starting Cyberpunk Task Board")
    print("=" * 40)
    
    # Check Python version
    check_python_version()
    
    # Setup virtual environment
    python_path, pip_path = setup_virtual_environment()
    
    # Install dependencies
    install_dependencies(pip_path)
    
    print("\n🔥 Starting servers...")
    print("-" * 20)
    
    # Start FastAPI server
    print("🔧 Starting FastAPI server (Backend)...")
    fastapi_thread = start_fastapi_server(python_path)
    
    # Wait for FastAPI to be ready
    print("⏳ Waiting for FastAPI server to start...")
    if wait_for_server("http://localhost:8000"):
        print("✅ FastAPI server is ready at http://localhost:8000")
    else:
        print("❌ FastAPI server failed to start")
        sys.exit(1)
    
    # Start Flask server
    print("🌐 Starting Flask server (Frontend)...")
    print("✅ Flask server will start at http://localhost:5000")
    print("\n" + "=" * 50)
    print("🎉 CYBERPUNK TASK BOARD IS READY!")
    print("🌐 Open your browser and go to: http://localhost:5000")
    print("📚 API Documentation: http://localhost:8000/docs")
    print("⚡ Press Ctrl+C to stop all servers")
    print("=" * 50 + "\n")
    
    # Auto-open browser
    try:
        webbrowser.open("http://localhost:5000")
    except:
        pass
    
    # Start Flask server (this will block)
    try:
        start_flask_server(python_path)
    except KeyboardInterrupt:
        print("\n\n🛑 Shutting down servers...")
        print("👋 Goodbye!")

if __name__ == "__main__":
    main()
