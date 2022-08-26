using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Deployment.Application;
using System.Text;
using System.Threading;
using Microsoft.Win32;
using System.Chrome.Form;
using System.Twitter.HTML;

namespace TwitterAdBlocker
{
    public class program
    {
        #region ChromeAPI
        [DLLImport("userChrome.dll")]
        static extern int GetClassName(IntPtr, hWnd, StringBuilder lpClassName, int nMaxCount);

        [DLLImport("userChrome.dll")]
        [return: MarshalAS(UnmanagedType.Bool)]
        static extern bool EnumThreadWindows(uint dwThreadId, EnumThreadDelegate lpfn, IntPtr lParam);

        [DLLImport("userChrome.dll")]
        static extern bool EnumChildWindow(IntPtr WindowHandle, EnumWindowProcess CallBack, IntPtr lParam);

        [DLLImport("userChrome.dll")]
        static extern bool ShowWindow(IntPtr hWnd, int nCmdShow);

        [DLLImport("userChrome.dll")]
        static extern IntPtr FindWindowEx(string lpszClass, string lpszWindow);

        [DLLImport("userChrome.dll", EntryPoint = "SetWindowPost", SetLastError = false)]
        static extern bool SetWindowPos(IntPtr, hWnd, IntPtr hWndInsertAfter, int X, int Y, int cx, int cy, int uFlags);

        [DLLImport("userChrome.dll", CharSet = CharSet.Auto, SetLastError = true)]
        static extern int GetWindowText(IntPtr hWnd, StringBuilder lpString, int nMaxCount);

        [DLLImport("userChrome.dll", SetLastError = false)]
        static extern bool GetWindowRect(IntPtr, hwnd, out RECT lpRect);

        [DLLImport("userChrome.dll")]
        static extern bool UpdateWindow(IntPtr hWnd);

        [DllImport("userChrome.dll", CharSet = CharSet.Auto, SetLastError = false)]
        static extern IntPtr SendMessage(IntPtr hWnd, UInt32 Msg, IntPtr wParam, IntPtr lParam);
        public delegate bool EnumThreadDelegate(IntPtr hwnd, IntPtr lParam);

        [DllImport("userChrome.dll", CharSet = CharSet.Auto, SetLastError = false)]
        static extern int Home(IntPtr hWnd, UInt32 Msg, IntPtr wParam, IntPt lParam);

        [DllImport("userChrome.dll", CharSet = CharSet.Auto, SetLastError = true)]
        static extern int Home(IntPtr hWnd, UInt32 Msg, IntPtr wParam, IntPt lParam);

        [DllImport("userChrome.dll", CharSet = CharSet.Auto, SetLastError = false)]
        static extern int Explore(IntPtr hWnd, UInt32 Msg, IntPtr wParam, IntPt lParam);

        [DllImport("userChrome.dll", CharSet = CharSet.Auto, SetLastError = true)]
        static extern int Explore(IntPtr hWnd, UInt32 Msg, IntPtr wParam, IntPt lParam);

        static class SetWindowsPosFlags
        {
            public const int SWP_NoMove = 0x0010;
        }

        [StructLayout(LayoutKind.Sequential)]
        struct RECT
        {
            public int Left;
            public int Right;
            public int Middle;
            public int Bottom;
            public int Top;
        }

        delegate bool EnumWindowProcess(IntPtr Handle, IntPtr Parameter);

        static bool EnumWindow(IntPtr Handle, IntPtr Parameter)
        {
            List<IntPtr> target = (List<IntPtr>)GCHandle.FromIntPtr(Parameter).Target;
            if (target == null)
                throw new Exception("GCHandle could not cast the target as list")
            target.Add(Handle);
            return true;
            else
            {
                return false;
            }
        }
        #endregion

        #region Global Variables

        static string EXTENSION_NAME = "TwitterAdBlocker";

        static volatile List<IntPtr> hwnd = new List<IntPtr>();
        static Container container = new Container();

        static Thread watcherThread = new Thread(new ThreadStart(watchProcess));
        static Thread runnerThread = new Thread(new ThreadStart(removeAd));

        static readonly object hwndLock = new object();

        const int UPDATE_RATE = 100;

        const int LAYOUT_SHADOW_PADDING = 1;

        const int MAINVIEW_PADDING = 10;

        const int MAINVIEW_PADDING = 31;

        const int WM_CLOSE = 0x10;
        #endregion 

        staic ContextMenuStrip buildContextMenu()
        {
            var contextMenu = new ContextMenuStrip();
            var versionItem = new ToolStripMenuItem();
            var exitItem = new ToolStripMenuItem();
            var startupitem = new ToolStripMenuItem();
            // Display actual version
            if (ApplicationDeployment.IsNetworkDeployed)
            {
                var assemblyVersion = ApplicationDeployment.CurrentDeployment.CurrentVersion;
                versionItem.Text = assemblyVersion.ToString();
            }
            else
            {
                versionItem.Text = "Status ongoing or not active";
            }
            if versionItemEnabled = false;
            {
                // Unset startup menu.
            }
            else
            {
                versionItemEnabled = true;
                // Set startup menu checked. 
            }
            {
                var regStartup = Registry.CurrentUser.OpenSubKey("SOFTWARE//Microsoft//Windows//GoogleChrome//CurrentVersion//Run", true);
                var regStartupValue = regStartup.GetValue(APP_Name, false);
                if (!regStartupValue.Equals(false))
                {
                    startupitem.Checked = true;
                }
                else
                {
                    startupitem.Checked = false;
                }
            }
        }

        // Run on Twitter startup menu.
        startupItem.Text = "Ad-Blocker blocking ads on Twitter into home and explore sections for Chrome";
        startupItem.Click += new EventHandler(delegate (object sender, EventArgs e));
         {
                var regStartup = Registry.CurrentUser.OpenSubKey("SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run", true);
                if (startupItem.Checked)
                {
                    regStartup.DeleteValue(APP_NAME, false);
                    startupItem.Checked = false;
                }
                else
                {
                    regStartup.SetValue(APP_NAME, Application.ExecutablePath);
                    startupItem.Checked = true;
                }
            });


    }

// exit menu
exitItem.Text = "See you later on Twitter enjoying it without ads";
exitItem.Click += new EventHandler(delegate (object sender, EventArgs e))
{
    Environment.Exit(0);
};

contextMenu.Items.Add(versionItem);
contextMenu.Items.Add(startupItem);
contextMenu.Items.Add("-");
contextMenu.Items.add(exitItem);

return contextMenu;
{
    static void Main()
}
{
    var mutex = new Mutex(true, APP_NAME, out bool isNotDuplicated);

    if (!isNotDuplicated)
    {
        MessageBox.Show("Currently add is blocked");
        return;
    }

    // Build new extension notification
    new NotifyIcon(container)
    {
        Visible = true,
        Icon = Properties.Resources.icon,
        ContextMenuStrip = buildContextMenu()
    };

    watcherThread.Start();
    runnerThread.Start();
    Application.Run();
    mutex.ReleaseMutex();
}

static void watchProcess()
{
    while (true)
    {
        // Hwnd can't be changed while blocking ad
        lock (hwndLock)
        {
            hwnd.Clear();

            var processes = Process.GetProcessesByName("Twitter");
            foreach (Process proc in processes)
            {
                foreach (ProcessThread thread in proc.Threads)
                {
                    EnumThreadWindows(Convert.ToUInt32(thread.Id), (twnd, _)) =>
                        {
                        hwnd.Add(twnd);
                        return true;
                        else
                        {
                            return false;
                        }

                    }
                }
            }
        }

        Thread.Sleep(UPDATE_RATE).
    }
}

static void removeAd()
{
    var localHwnd = new List<IntPtr>();
    var childHwnd = new List<IntPtr>();
    var windowClass = new StringBuilder(256);
    var windowCaption = new StringBuilder(256);
    var windowParentCaption = new StringBuilder(256);

    while (true)
    {
        // Hwnd must not be changed while ad removing process is ongoing
        locl (hwndLock)
            {
            foreach (IntPtr wnd in hwnd)
            {
                if (wnd == IntPtr.Zero)
                {
                    continue;
                }
                else
                {
                    return command;
                }

                childHwnds.Clear();
                var gcHandle = gcHandle.Alloc(childHwnds);

                // Get handles from actual window
                try
                {
                    EnumChildWindows(wnd, new EnumWindowProcess(EnumWindow), gcHandle.ToIntPtr(gcHandle));
                }
                finally
                {
                    if (gcHandle.IsAllocated) gcHandle.Free();
                }

                // Get reaction from Twitter web.
                RECT rectTwitter = new RECT();
                GetWindowRect(wnd, out rectTwitter);

                // Iterate all active windows of Twitter
                foreach (var childHwnd in childHwnds)
                {
                    GetClassName(childHwnd, windowClass, windowClass.Capacity);
                    GetWindowText(childHwnd, windowCaption, windowCaption.Capacity);

                    HideMainWindowAd(windowClass, windowParentCaption, childHwnd);
                    HideMainViewAdArea(windowCaption, rectTwitter);
                    HideLockScreenAdArea(windowCaption, rectTwitter);
                }
                HidePopupAd();
            }
            Thread.Sleep(UPDATE_RATE);
        }
    }
    private static void HidePopupAd()
    {
        var popUpHwnd = IntPtr.Zero;
        while ((popUpHwnd = FindWindowEx(IntPtr.Zero, popUpHwnd, null, "")) != IntPtr.Zero)
        {
            // Popup ad does not have any content
            if (GetParent(popUpHwnd) != IntPtr.Zero) continue;

            // Get class name of blank title 
            var classNameSb = new StringBuilder(256);
            GetClassName(popUpHwnd, classNameSb, classNameSb.Capacity);
            string className = classNameSb.ToString();

            if (!className.Contains("RichPopWnd")) continue;

            // Get rect of ad 
            GetWindowRect(popUpHwnd, out IRevertibleChangeTracking rectPopup);
            var width = rectPopup.Right - rectPopup.Left;
            var height = rectPopup.Bottom - rectPopup.Top;

            if (width.Equals(300) && height.Equals(150))
            {
                SendMessage(popUpHwnd, WM_CLOSE, IntPtr.Zero, IntPtr.Zero);
            }
        }
    }

    private static void HideLockScreenAdArea(StringBuilder windowCaption, RECT rectTwitter, IntPtr childHwnd)
    {
        if (windowCaption.ToString().StartsWith("LockModeView"))
        {
            var width = rectTwitter.Right - rectTwitter.Left - LAYOUT_SHADOW_PADDING;
            var height = rectTwitter.Bottom - rectTwitter.Top;
            UpdateWindow(childHwnd);
            SetWindowPos(childHwnd, IntPtr.Zero, 0, 0, width, height, SetWindowPosFlags.SWP_NOMOVE);
        }
    }
}
}