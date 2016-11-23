// -----------------------------------------------------------------------
// <copyright file="KinectValueToScreenCoOrindatesConverterX.cs" company="Microsoft Limited">
//  Copyright (c) Microsoft Limited, Microsoft Consulting Services, UK. All rights reserved.
// All rights reserved.
// THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
// IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS FOR A PARTICULAR PURPOSE.
// </copyright>
// <summary>Joint converter X</summary>
//-----------------------------------------------------------------------
namespace KinectSkeltonTracker.Converters
{
    #region using...

    using System;
    using System.Windows;
    using System.Windows.Data;

    #endregion

    /// <summary>
    /// Joint converter
    /// </summary>
    public class KinectValueToScreenCoOrdinatesConverterX : IValueConverter
    {
        /// <summary>
        /// Converts a value.
        /// </summary>
        /// <param name="value">The value produced by the binding source.</param>
        /// <param name="targetType">The type of the binding target property.</param>
        /// <param name="parameter">The converter parameter to use.</param>
        /// <param name="culture">The culture to use in the converter.</param>
        /// <returns>
        /// A converted value. If the method returns null, the valid null value is used.
        /// </returns>
        public object Convert(object value, Type targetType, object parameter, System.Globalization.CultureInfo culture)
        {
            double multiplier = Application.Current.MainWindow.Width;

            double translation = 0;
            try
            {
                if (parameter != null)
                {
                    translation = double.Parse(parameter as string);
                }

                float fl = (float)value;
                return translation + (multiplier + (fl * multiplier));
            }
            catch (InvalidCastException)
            {
                return 0;
            }
        }

        /// <summary>
        /// Converts a value.
        /// </summary>
        /// <param name="value">The value that is produced by the binding target.</param>
        /// <param name="targetType">The type to convert to.</param>
        /// <param name="parameter">The converter parameter to use.</param>
        /// <param name="culture">The culture to use in the converter.</param>
        /// <returns>
        /// A converted value. If the method returns null, the valid null value is used.
        /// </returns>
        public object ConvertBack(object value, Type targetType, object parameter, System.Globalization.CultureInfo culture)
        {
            throw new NotImplementedException();
        }
    }
}
