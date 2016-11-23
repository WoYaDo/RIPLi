// -----------------------------------------------------------------------
// <copyright file="MenuSegments.cs" company="Microsoft Limited">
//  Copyright (c) Microsoft Limited, Microsoft Consulting Services, UK. All rights reserved.
// All rights reserved.
// THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
// IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS FOR A PARTICULAR PURPOSE.
// </copyright>
// <summary>The menu gesture segment</summary>
//-----------------------------------------------------------------------
namespace KinectSkeltonTracker.Gestures.GestureParts
{
    #region using...

    using Microsoft.Research.Kinect.Nui;

    #endregion

    /// <summary>
    /// The menu gesture segment
    /// </summary>
    public class MenuSegments1 : IRelativeGestureSegment
    {
        /// <summary>
        /// Checks the gesture.
        /// </summary>
        /// <param name="skeleton">The skeleton.</param>
        /// <returns>GesturePartResult based on if the gesture part has been completed</returns>
        public GesturePartResult CheckGesture(Microsoft.Research.Kinect.Nui.SkeletonData skeleton)
        {
            // Left and right hands below hip
            if (skeleton.Joints[JointID.HandLeft].Position.Y < skeleton.Joints[JointID.HipCenter].Position.Y && skeleton.Joints[JointID.HandRight].Position.Y < skeleton.Joints[JointID.HipCenter].Position.Y)
            {
                // left hand 0.3 to left of center hip
                if (skeleton.Joints[JointID.HandLeft].Position.X < skeleton.Joints[JointID.HipCenter].Position.X - 0.3)
                {
                    // left hand 0.2 to left of left elbow
                    if (skeleton.Joints[JointID.HandLeft].Position.X < skeleton.Joints[JointID.ElbowLeft].Position.X - 0.2)
                    {
                        return GesturePartResult.Suceed;
                    }
                }

                return GesturePartResult.Pausing;
            }

            return GesturePartResult.Fail;
        }
    }
}
