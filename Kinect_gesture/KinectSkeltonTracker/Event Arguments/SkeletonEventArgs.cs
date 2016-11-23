// -----------------------------------------------------------------------
// <copyright file="SkeletonEventArgs.cs" company="Microsoft Limited">
//  Copyright (c) Microsoft Limited, Microsoft Consulting Services, UK. All rights reserved.
// All rights reserved.
// THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
// IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS FOR A PARTICULAR PURPOSE.
// </copyright>
// <summary>The skeleton event args</summary>
//-----------------------------------------------------------------------
namespace KinectSkeltonTracker
{
    #region using...

    using System;
    using Microsoft.Research.Kinect.Nui;

    #endregion

    /// <summary>
    /// The skeleton event args
    /// </summary>
    public class SkeletonEventArgs : EventArgs
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="SkeletonEventArgs"/> class.
        /// </summary>
        /// <param name="skeleton">The skeleton.</param>
        public SkeletonEventArgs(SkeletonData skeleton)
        {
            this.Skeleton = skeleton;
        }

        /// <summary>
        /// Gets or sets the skeleton.
        /// </summary>
        /// <value>
        /// The skeleton.
        /// </value>
        public SkeletonData Skeleton
        { 
            get; 
            set; 
        }
    }
}
