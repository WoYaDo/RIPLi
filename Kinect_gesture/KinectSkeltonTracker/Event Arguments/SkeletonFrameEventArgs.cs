// -----------------------------------------------------------------------
// <copyright file="SkeletonFrameEventArgs.cs" company="Microsoft Limited">
//  Copyright (c) Microsoft Limited, Microsoft Consulting Services, UK. All rights reserved.
// All rights reserved.
// THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
// IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS FOR A PARTICULAR PURPOSE.
// </copyright>
// <summary>The skeleton frame event args</summary>
//-----------------------------------------------------------------------
namespace KinectSkeltonTracker
{
    #region using...

    using System;
    using System.Collections.Generic;

    #endregion

    /// <summary>
    /// The skeleton frame event args
    /// </summary>
    public class SkeletonFrameEventArgs : EventArgs
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="SkeletonFrameEventArgs"/> class.
        /// </summary>
        /// <param name="skeletonIDValues">The skeleton ID values.</param>
        /// <param name="timeStamp">The time stamp.</param>
        public SkeletonFrameEventArgs(List<int> skeletonIDValues, long timeStamp)
        {
            this.SkeletonIDValues = skeletonIDValues;
            this.TimeStamp = timeStamp;
        }

        /// <summary>
        /// Gets or sets the skeleton ID values.
        /// </summary>
        /// <value>
        /// The skeleton ID values.
        /// </value>
        public List<int> SkeletonIDValues
        {
            get;
            set;
        }

        /// <summary>
        /// Gets or sets the time stamp.
        /// </summary>
        /// <value>
        /// The time stamp.
        /// </value>
        public long TimeStamp
        {
            get;
            set;
        }
    }
}
