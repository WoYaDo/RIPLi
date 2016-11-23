//-----------------------------------------------------------------------
// <copyright file="KinectConnection.cs" company="Microsoft Limited">
// Copyright (c) Microsoft Limited, Microsoft Consulting Services, UK. All rights reserved.
// All rights reserved.
// THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
// IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS FOR A PARTICULAR PURPOSE.
// </copyright>
// <summary>The kinect connection class</summary>
//-----------------------------------------------------------------------
namespace KinectSkeltonTracker
{
    #region using...

    using System;
    using System.Collections.Generic;
    using System.Windows.Documents;
    using Microsoft.Research.Kinect.Nui;

    #endregion

    /// <summary>
    /// The kinect connection class
    /// </summary>
    public class KinectConnection
    {
        /// <summary>
        /// The list of approved camera angles
        /// </summary>
        private static readonly int[] cameraAngles = { -25, -23, -21, -19, -17, -15, -13, -11, -9, -7, -5, -3, -1, 0, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25 };

        /// <summary>
        /// The Kinect run time
        /// </summary>
        private Runtime kinectRunTime = new Runtime();

        /// <summary>
        /// The current index of the angle that the sensor is at
        /// </summary>
        private int currentAngle;
        
        /// <summary>
        /// Initializes a new instance of the <see cref="KinectConnection"/> class.
        /// </summary>
        public KinectConnection()
        {
            if (this.InitializeNui())
            {
                this.kinectRunTime.SkeletonFrameReady += new EventHandler<SkeletonFrameReadyEventArgs>(this.KinectRunTime_SkeletonFrameReady);
                this.kinectRunTime.VideoFrameReady += new EventHandler<ImageFrameReadyEventArgs>(this.KinectRunTime_VideoFrameReady);

                if (this.kinectRunTime.NuiCamera.ElevationAngle != cameraAngles[13])
                {
                    this.kinectRunTime.NuiCamera.ElevationAngle = cameraAngles[13];
                    this.currentAngle = 12;
                }
            }
            else
            {
                throw new Exception("Error initialising Kinect sensor");
            }
        }

        /// <summary>
        /// Occurs when [skeleton ready].
        /// </summary>
        public event EventHandler<SkeletonEventArgs> SkeletonReady;

        /// <summary>
        /// Occurs when [image frame ready].
        /// </summary>
        public event EventHandler<ImageFrameReadyEventArgs> ImageFrameReady;

        /// <summary>
        /// Occurs when [skeleton frame complete].
        /// </summary>
        public event EventHandler<SkeletonFrameEventArgs> SkeletonFrameComplete;

        /// <summary>
        /// Tilts the camera up.
        /// </summary>
        /// <returns> bool value true if the sensore moved</returns>
        public bool TiltUp()
        {
            if (this.currentAngle >= cameraAngles.Length)
            {
                return false;
            }

            try
            {
                this.currentAngle += 1;
                this.kinectRunTime.NuiCamera.ElevationAngle = cameraAngles[this.currentAngle];
                return true;
            }
            catch (InvalidOperationException)
            {
                this.currentAngle -= 1;
                return false;
            }
        }

        /// <summary>
        /// Tilts the camera down.
        /// </summary>
        /// <returns>bool value true if the sensore moved</returns>
        public bool TiltDown()
        {
            if (this.currentAngle <= 0)
            {
                return false;
            }

            try
            {
                this.currentAngle -= 1;
                this.kinectRunTime.NuiCamera.ElevationAngle = cameraAngles[this.currentAngle];
                return true;
            }
            catch (InvalidOperationException)
            {
                this.currentAngle += 1;
                return false;
            }
        }

        /// <summary>
        /// Handles the VideoFrameReady event of the kinectRunTime control.
        /// </summary>
        /// <param name="sender">The source of the event.</param>
        /// <param name="e">The <see cref="Microsoft.Research.Kinect.Nui.ImageFrameReadyEventArgs"/> instance containing the event data.</param>
        private void KinectRunTime_VideoFrameReady(object sender, ImageFrameReadyEventArgs e)
        {
            if (this.ImageFrameReady != null)
            {
                this.ImageFrameReady(this, e);
            }
        }

        /// <summary>
        /// Handles the SkeletonFrameReady event of the kinectRunTime control.
        /// </summary>
        /// <param name="sender">The source of the event.</param>
        /// <param name="e">The <see cref="Microsoft.Research.Kinect.Nui.SkeletonFrameReadyEventArgs"/> instance containing the event data.</param>
        private void KinectRunTime_SkeletonFrameReady(object sender, SkeletonFrameReadyEventArgs e)
        {
            List<int> idValues = new List<int>();

            if (e.SkeletonFrame.Skeletons.Length >= 1)
            {
                int trackingCount = 0;
              
                while (trackingCount < e.SkeletonFrame.Skeletons.Length)
                {
                    if (e.SkeletonFrame.Skeletons[trackingCount].TrackingState == SkeletonTrackingState.Tracked)
                    {
                        if (this.SkeletonReady != null)
                        {
                            this.SkeletonReady(this, new SkeletonEventArgs(e.SkeletonFrame.Skeletons[trackingCount]));
                        }
                        
                        idValues.Add(e.SkeletonFrame.Skeletons[trackingCount].TrackingID);
                    }

                    trackingCount++;
                    
                    if (this.SkeletonFrameComplete != null)
                    {
                        this.SkeletonFrameComplete(this, new SkeletonFrameEventArgs(idValues, e.SkeletonFrame.TimeStamp));
                    }
                }
            }
        }

        /// <summary>
        /// Initializes the Kinect sensor.
        /// </summary>
        /// <returns>bool value true if the sensor initialised correctly</returns>
        private bool InitializeNui()
        {
            if (this.kinectRunTime == null)
            {
                return false;
            }

            try
            {
                this.kinectRunTime.Initialize(RuntimeOptions.UseDepth | RuntimeOptions.UseSkeletalTracking | RuntimeOptions.UseColor);
            }
            catch (Exception exception)
            {
                Console.WriteLine(exception.ToString());
                return false;
            }

            this.kinectRunTime.VideoStream.Open(ImageStreamType.Video, 2, ImageResolution.Resolution640x480, ImageType.Color);

            this.kinectRunTime.SkeletonEngine.TransformSmooth = true;

            var parameters = new TransformSmoothParameters
            {
                Smoothing = 0.75f,
                Correction = 0.0f,
                Prediction = 0.0f,
                JitterRadius = 0.05f,
                MaxDeviationRadius = 0.04f
            };

            this.kinectRunTime.SkeletonEngine.SmoothParameters = parameters;

            return true;
        }
    }
}
