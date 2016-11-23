﻿// -----------------------------------------------------------------------
// <copyright file="MainWindow.xaml.cs" company="Microsoft Limited">
//  Copyright (c) Microsoft Limited, Microsoft Consulting Services, UK. All rights reserved.
// All rights reserved.
// THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
// IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS FOR A PARTICULAR PURPOSE.
// </copyright>
// <summary>Interaction logic for MainWindow.xaml</summary>
//-----------------------------------------------------------------------
namespace KinectSkeltonTracker
{
    #region using...

    using System;
    using System.Windows;
    using System.Windows.Media;
    using System.Windows.Media.Imaging;
    using Microsoft.Research.Kinect.Nui;
    using System.IO.Pipes;
    using System.IO;
    using System.Text;

    #endregion

    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        static NamedPipeServerStream server;
        static BinaryWriter bw;
        /// <summary>
        /// Initializes a new instance of the <see cref="MainWindow"/> class.
        /// </summary>
        public MainWindow()
        {
            server = new NamedPipeServerStream("NPtest");
            Console.WriteLine("Waiting for connection...");
            server.WaitForConnection();

            Console.WriteLine("Connected.");
            bw = new BinaryWriter(server);

            InitializeComponent();
            MainViewModel model = new MainViewModel();
            this.DataContext = model;
            this.SkeletonControl.ItemsSource = model.Skeletons;
            model.Kinect.ImageFrameReady += new EventHandler<Microsoft.Research.Kinect.Nui.ImageFrameReadyEventArgs>(this.Kinect_ImageFrameReady);
        }

        public static void WriteToBuffer(String str)
        {
            var buf = Encoding.ASCII.GetBytes(str);     // Get ASCII byte array     
            bw.Write((uint)buf.Length);                // Write string length
            bw.Write(buf);                              // Write string
            Console.WriteLine("Wrote: \"{0}\"", str);
        }

        /// <summary>
        /// Handles the ImageFrameReady event of the kinect control.
        /// </summary>
        /// <param name="sender">The source of the event.</param>
        /// <param name="e">The <see cref="Microsoft.Research.Kinect.Nui.ImageFrameReadyEventArgs"/> instance containing the event data.</param>
        private void Kinect_ImageFrameReady(object sender, Microsoft.Research.Kinect.Nui.ImageFrameReadyEventArgs e)
        {
            PlanarImage image = e.ImageFrame.Image;
            cameraFeed.Source = BitmapSource.Create(image.Width, image.Height, 96, 96, PixelFormats.Bgr32, null, image.Bits, image.Width * image.BytesPerPixel);
        }
    }
}
