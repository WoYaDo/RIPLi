// -----------------------------------------------------------------------
// <copyright file="MainViewModel.cs" company="Microsoft Limited">
//  Copyright (c) Microsoft Limited, Microsoft Consulting Services, UK. All rights reserved.
// All rights reserved.
// THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
// IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS FOR A PARTICULAR PURPOSE.
// </copyright>
// <summary>The main view model</summary>
//-----------------------------------------------------------------------
namespace KinectSkeltonTracker
{
    #region using...

    using System;
    using System.Collections.Generic;
    using System.Collections.ObjectModel;
    using System.ComponentModel;
    using System.Windows.Media;

    #endregion

    /// <summary>
    /// The main view model
    /// </summary>
    public class MainViewModel : INotifyPropertyChanged
    {
        /// <summary>
        /// The available colors for the skeleton
        /// </summary>
        private static readonly Color[] availableColors = { Colors.Red, Colors.Blue, Colors.Green, Colors.Orange, Colors.Purple };

        /// <summary>
        /// The current color id
        /// </summary>
        private static int colorID = 0;

        /// <summary>
        /// the dictionary of skeletons
        /// </summary>
        private Dictionary<int, SkeletonViewModel> skeletonDictionary = new Dictionary<int, SkeletonViewModel>();

        /// <summary>
        /// Initializes a new instance of the <see cref="MainViewModel"/> class.
        /// </summary>
        public MainViewModel()
        {
            this.Kinect = new KinectConnection();
            this.Skeletons = new ObservableCollection<SkeletonViewModel>();
            this.Kinect.SkeletonReady += new EventHandler<SkeletonEventArgs>(this.Kinect_SkeletonReady);
        }

        /// <summary>
        /// Occurs when a property value changes.
        /// </summary>
        public event PropertyChangedEventHandler PropertyChanged;

        /// <summary>
        /// Gets or sets the kinect connection.
        /// </summary>
        /// <value>
        /// The kinect connection.
        /// </value>
        public KinectConnection Kinect
        {
            get;
            set;
        }

        /// <summary>
        /// Gets or sets the skeletons.
        /// </summary>
        /// <value>
        /// The skeletons.
        /// </value>
        public ObservableCollection<SkeletonViewModel> Skeletons
        {
            get;
            set;
        }

        /// <summary>
        /// Handles the SkeletonReady event of the kinect control.
        /// </summary>
        /// <param name="sender">The source of the event.</param>
        /// <param name="e">The <see cref="KinectSkeltonTracker.SkeletonEventArgs"/> instance containing the event data.</param>
        private void Kinect_SkeletonReady(object sender, SkeletonEventArgs e)
        {
            if (this.skeletonDictionary.ContainsKey(e.Skeleton.TrackingID))
            {
                this.skeletonDictionary[e.Skeleton.TrackingID].Skeleton = e.Skeleton;
                this.skeletonDictionary[e.Skeleton.TrackingID].ResetTimer();
            }
            else
            {
                SkeletonViewModel viewModel = new SkeletonViewModel();
                viewModel.Skeleton = e.Skeleton;
                viewModel.JointColor = availableColors[colorID];
                if (colorID == availableColors.Length - 1)
                {
                    colorID = 0;
                }
                else
                {
                    colorID += 1;
                }

                this.skeletonDictionary.Add(e.Skeleton.TrackingID, viewModel);
                this.Skeletons.Add(viewModel);
                viewModel.DeleteSkeleton += new EventHandler(this.ViewModel_DeleteSkeleton);
            }
        }

        /// <summary>
        /// Handles the DeleteSkeleton event of the ViewModel control.
        /// </summary>
        /// <param name="sender">The source of the event.</param>
        /// <param name="e">The <see cref="System.EventArgs"/> instance containing the event data.</param>
        private void ViewModel_DeleteSkeleton(object sender, EventArgs e)
        {
            SkeletonViewModel model = sender as SkeletonViewModel;
            if (model != null)
            {
                this.Skeletons.Remove(model);
                this.skeletonDictionary.Remove(model.Skeleton.TrackingID);
            }
        }
        
        /// <summary>
        /// Notifies the property changed.
        /// </summary>
        /// <param name="propertyName">Name of the property.</param>
        private void NotifyPropertyChanged(string propertyName)
        {
            if (this.PropertyChanged != null)
            {
                this.PropertyChanged(this, new PropertyChangedEventArgs(propertyName));
            }
        }
    }
}
